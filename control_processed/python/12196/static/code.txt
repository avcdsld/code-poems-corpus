def bbox_flip(bbox, d, rows, cols):
    """Flip a bounding box either vertically, horizontally or both depending on the value of `d`.

    Raises:
        ValueError: if value of `d` is not -1, 0 or 1.

    """
    if d == 0:
        bbox = bbox_vflip(bbox, rows, cols)
    elif d == 1:
        bbox = bbox_hflip(bbox, rows, cols)
    elif d == -1:
        bbox = bbox_hflip(bbox, rows, cols)
        bbox = bbox_vflip(bbox, rows, cols)
    else:
        raise ValueError('Invalid d value {}. Valid values are -1, 0 and 1'.format(d))
    return bbox