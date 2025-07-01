def resize(image, width, height, channels=None, decode=False,
           resample='nearest'):
    """
    Resizes the image or SArray of Images to a specific width, height, and
    number of channels.

    Parameters
    ----------

    image : turicreate.Image | SArray
        The image or SArray of images to be resized.
    width : int
        The width the image is resized to.
    height : int
        The height the image is resized to.
    channels : int, optional
        The number of channels the image is resized to. 1 channel
        corresponds to grayscale, 3 channels corresponds to RGB, and 4
        channels corresponds to RGBA images.
    decode : bool, optional
        Whether to store the resized image in decoded format. Decoded takes
        more space, but makes the resize and future operations on the image faster.
    resample : 'nearest' or 'bilinear'
        Specify the resampling filter:

            - ``'nearest'``: Nearest neigbhor, extremely fast
            - ``'bilinear'``: Bilinear, fast and with less aliasing artifacts

    Returns
    -------
    out : turicreate.Image
        Returns a resized Image object.

    Notes
    -----
    Grayscale Images -> Images with one channel, representing a scale from
    white to black

    RGB Images -> Images with 3 channels, with each pixel having Green, Red,
    and Blue values.

    RGBA Images -> An RGB image with an opacity channel.

    Examples
    --------

    Resize a single image

    >>> img = turicreate.Image('https://static.turi.com/datasets/images/sample.jpg')
    >>> resized_img = turicreate.image_analysis.resize(img,100,100,1)

    Resize an SArray of images

    >>> url ='https://static.turi.com/datasets/images/nested'
    >>> image_sframe = turicreate.image_analysis.load_images(url, "auto", with_path=False,
    ...                                                    recursive=True)
    >>> image_sarray = image_sframe["image"]
    >>> resized_images = turicreate.image_analysis.resize(image_sarray, 100, 100, 1)
    """

    if height < 0 or width < 0:
        raise ValueError("Cannot resize to negative sizes")

    if resample == 'nearest':
        resample_method = 0
    elif resample == 'bilinear':
        resample_method = 1
    else:
        raise ValueError("Unknown resample option: '%s'" % resample)

    from ...data_structures.sarray import SArray as _SArray
    from ... import extensions as _extensions
    if type(image) is _Image:
        if channels is None:
            channels = image.channels
        if channels <= 0:
            raise ValueError("cannot resize images to 0 or fewer channels")
        return _extensions.resize_image(image, width, height, channels, decode, resample_method)
    elif type(image) is _SArray:
        if channels is None:
            channels = 3
        if channels <= 0:
            raise ValueError("cannot resize images to 0 or fewer channels")
        return image.apply(lambda x: _extensions.resize_image(x, width, height, channels, decode, resample_method))
    else:
        raise ValueError("Cannot call 'resize' on objects that are not either an Image or SArray of Images")