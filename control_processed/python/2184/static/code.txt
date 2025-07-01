def _value_counts_arraylike(values, dropna):
    """
    Parameters
    ----------
    values : arraylike
    dropna : boolean

    Returns
    -------
    (uniques, counts)

    """
    values = _ensure_arraylike(values)
    original = values
    values, dtype, ndtype = _ensure_data(values)

    if needs_i8_conversion(dtype):
        # i8

        keys, counts = htable.value_count_int64(values, dropna)

        if dropna:
            msk = keys != iNaT
            keys, counts = keys[msk], counts[msk]

    else:
        # ndarray like

        # TODO: handle uint8
        f = getattr(htable, "value_count_{dtype}".format(dtype=ndtype))
        keys, counts = f(values, dropna)

        mask = isna(values)
        if not dropna and mask.any():
            if not isna(keys).any():
                keys = np.insert(keys, 0, np.NaN)
                counts = np.insert(counts, 0, mask.sum())

    keys = _reconstruct_data(keys, original.dtype, original)

    return keys, counts