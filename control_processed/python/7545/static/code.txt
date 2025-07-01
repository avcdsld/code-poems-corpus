def parse_data_shape(data_shape_str):
    """Parse string to tuple or int"""
    ds = data_shape_str.strip().split(',')
    if len(ds) == 1:
        data_shape = (int(ds[0]), int(ds[0]))
    elif len(ds) == 2:
        data_shape = (int(ds[0]), int(ds[1]))
    else:
        raise ValueError("Unexpected data_shape: %s", data_shape_str)
    return data_shape