def bbox_vflip(bbox, rows, cols):
    """Flip a bounding box vertically around the x-axis."""
    x_min, y_min, x_max, y_max = bbox
    return [x_min, 1 - y_max, x_max, 1 - y_min]