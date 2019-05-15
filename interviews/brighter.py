"""
Author: Srinath Kailasa
Date: 22 November 2018

Example Usage:
>>> import glob
>>>
>>> # directory where images are stored
>>> filepaths = glob.glob('/image_dir/*.jpg')
>>>
>>> # instantiate processor object with desired functionality
>>> processer = ImageProcessor(find_random_patch)
>>>
>>> # call process method to return generator, declare optional args
>>> processsed_images = processer.process(filepaths, run_forever=True, random_order=True)
>>>
>>> # generator returns batches of processed images
>>> for batch in processed_images:
>>> ...    print(batch)
"""
import itertools

import numpy as np


def shuffle_generator(_list):
    """
    Return a generator of a given input list with a randomly permuted
        order.
    :param list _list: A list to randomly permute.
    :return generator: A generator of a given list in a randomly
        permuted order.
    """
    return (_list[idx] for idx in np.random.permutation(len(_list)))


def batch(iterable, batch_size):
    """
    Generator returning batches of an input iterable, of size
        batch_size.
    :param iter iterable: The iterable being batched.
    :param int batch_size: The batch size.
    :return: Yields batches of input iterable.
    """
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, batch_size))
        if not chunk:
            return
        yield chunk


def load_image(filepath):
    """
    A fake image loading function, this was just to test the processing
        code with as I haven't been provided with an image format. In
        reality it would be used for reading an image into a numpy array
        from a given filepath.
    :param str filepath: Pointer to where an image is saved on disk.
    :return np.array: A numpy array containing the image.
    """
    return np.ones((1920, 1080, 3))


def find_random_patch(array, xdim=1920, ydim=1080, patch_size=512):
    """
    Find a random square patch in the image.
    :param np.array array: The array from which to find the patch.
    :param int xdim: The x dimension of the array.
    :param int ydim: The y dimension of the array.
    :param int patch_size: The dimension of the square patch.
    :return np.array: A random square patch of the array.
    """
    patch = None
    found = False
    nrgb = 3  # number of rgb colours, the z-dimension of the array

    while not found:
        x_rand = np.random.randint(low=0, high=xdim-patch_size)
        y_rand = np.random.randint(low=0, high=ydim-patch_size)
        patch = array[x_rand:x_rand + patch_size, y_rand:y_rand + patch_size, :]
        if patch.shape == (patch_size, patch_size, nrgb):
            found = True

    return patch


class ImageProcessor:
    """
    Use class to abstract processing function from desired generator
        containing processed images.
    """

    def __init__(self, processing_func):
        """
        :param func processing_func: The function being used to process
            the images. Takes an image array as an argument.
        """
        self._processing_func = processing_func

    def process(self, filepaths, run_forever=False, random_order=False):
        """
        Generator, processing the images. Processing is done in batches
            to conserve memory with large image datasets.
        :param list[str] filepaths: List of filepaths of images being
            processed.
        :param bool run_forever: If True will run for ever, otherwise
            runs once. When running forever, the process order will be
            the same each time, unless random_order is also set to True
        :param bool random_order: If True will process batch in random
            order.
        :return: Yield processed batches, using the instantiated
            processing function.
        """
        batch_size = 5

        end = False

        while not end:
            if not random_order:
                batched_filepaths = batch(filepaths, batch_size)
            else:
                batched_filepaths = batch(
                    shuffle_generator(filepaths), batch_size
                )

            for batch_of_filepaths in batched_filepaths:
                print(batch_of_filepaths)
                yield np.array([
                    self._processing_func(load_image(filepath))
                    for filepath in batch_of_filepaths
                ])

            if not run_forever:
                end = True


if __name__ == "__main__":
    fps = ['a', 'b', 'c', 'd', 'e']
    p = ImageProcessor(find_random_patch)

    processed = p.process(fps, random_order=False, run_forever=True)

    for i in processed:
        print(i.shape)
