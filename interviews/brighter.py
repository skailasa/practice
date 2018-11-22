"""
Write an iterator in Python.
- reads in all data, pre-processing so that it's suitable for
    machine learning models.
Task:
- Consider image datasets with images of resolution 1920x1080, passed to
    the generator as a list of paths pointing to the location on disk.
- The iterator should read in the original images from disk and randomly
    select one 512x512 patch in the image.
- Once 32 images have been processed, it should yield a batch of 32
    patches.
- i.e. The iterator serves numpy arrays of dimension 32x3x512x512.
- An input image is only used once for selecting a patch, until all
    input images are processed.
- Should also have the option of running forever, in which case after
    each input images are used it starts again.
- The generator should also have the option to to process input images
    in a random order. In the instance of it running forever, the order
    should be different for each pass through the dataset.
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
    Generator returning batches of an input iterable, of size batch_size.
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
    """

    def __init__(self, processing_func):
        """
        :param func processing_func: The function being used to process
            the images. Takes an image array as an argument.
        """
        self._processing_func = processing_func

    def process(self, filepaths, run_forever=False, random_order=False):
        """
        Generator, processing the images. Takes list of input filepaths,
            yields random patches.
        :param list[str] filepaths: List of filepaths of images being
            processed.
        :param bool run_forever: If True will run for ever, and vice
            versa. If random_order also set to true, will pick run
            batches in a different order each time.
        :param bool random_order: If True will process batch in random
            order.
        :return: Yield processed batches of dimension (batchsize, 512, 512, 3)
        """
        batch_size = 32

        end = False

        while not end:
            if not random_order:
                batched_filepaths = batch(filepaths, batch_size)
            else:
                batched_filepaths = batch(shuffle_generator(filepaths), batch_size)

            for batch_of_filepaths in batched_filepaths:
                yield np.array([
                    self._processing_func(load_image(filepath))
                    for filepath in batch_of_filepaths
                ])

            if not run_forever:
                end = True


if __name__ == "__main__":

    filepaths = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    processer = ImageProcessor(find_random_patch).process(filepaths)

    for i in processer:
        print(i.shape)