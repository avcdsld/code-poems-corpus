def _decode(image_data):
    """
    Internal helper function for decoding a single Image or an SArray of Images
    """
    from ...data_structures.sarray import SArray as _SArray
    from ... import extensions as _extensions
    if type(image_data) is _SArray:
        return _extensions.decode_image_sarray(image_data)
    elif type(image_data) is _Image:
        return _extensions.decode_image(image_data)