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
