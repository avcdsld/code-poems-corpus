def mask_missing(arr, values_to_mask):
    """
    Return a masking array of same size/shape as arr
    with entries equaling any member of values_to_mask set to True
    """
    dtype, values_to_mask = infer_dtype_from_array(values_to_mask)

    try:
        values_to_mask = np.array(values_to_mask, dtype=dtype)

    except Exception:
        values_to_mask = np.array(values_to_mask, dtype=object)

    na_mask = isna(values_to_mask)
    nonna = values_to_mask[~na_mask]

    mask = None
    for x in nonna:
        if mask is None:

            # numpy elementwise comparison warning
            if is_numeric_v_string_like(arr, x):
                mask = False
            else:
                mask = arr == x

            # if x is a string and arr is not, then we get False and we must
            # expand the mask to size arr.shape
            if is_scalar(mask):
                mask = np.zeros(arr.shape, dtype=bool)
        else:

            # numpy elementwise comparison warning
            if is_numeric_v_string_like(arr, x):
                mask |= False
            else:
                mask |= arr == x

    if na_mask.any():
        if mask is None:
            mask = isna(arr)
        else:
            mask |= isna(arr)

    # GH 21977
    if mask is None:
        mask = np.zeros(arr.shape, dtype=bool)

    return mask