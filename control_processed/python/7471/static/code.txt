def bbox_flip(bbox, width, flip_x=False):
    """
    invalid value in bbox_transform if this wrong (no overlap), note index 0 and 2
    also note need to save before assignment
    :param bbox: [n][x1, y1, x2, y2]
    :param width: cv2 (height, width, channel)
    :param flip_x: will flip x1 and x2
    :return: flipped box
    """
    if flip_x:
        xmax = width - bbox[:, 0]
        xmin = width - bbox[:, 2]
        bbox[:, 0] = xmin
        bbox[:, 2] = xmax
    return bbox