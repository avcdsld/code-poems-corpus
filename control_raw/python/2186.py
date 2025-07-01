def mode(values, dropna=True):
    """
    Returns the mode(s) of an array.

    Parameters
    ----------
    values : array-like
        Array over which to check for duplicate values.
    dropna : boolean, default True
        Don't consider counts of NaN/NaT.

        .. versionadded:: 0.24.0

    Returns
    -------
    mode : Series
    """
    from pandas import Series

    values = _ensure_arraylike(values)
    original = values

    # categorical is a fast-path
    if is_categorical_dtype(values):
        if isinstance(values, Series):
            return Series(values.values.mode(dropna=dropna), name=values.name)
        return values.mode(dropna=dropna)

    if dropna and is_datetimelike(values):
        mask = values.isnull()
        values = values[~mask]

    values, dtype, ndtype = _ensure_data(values)

    f = getattr(htable, "mode_{dtype}".format(dtype=ndtype))
    result = f(values, dropna=dropna)
    try:
        result = np.sort(result)
    except TypeError as e:
        warn("Unable to sort modes: {error}".format(error=e))

    result = _reconstruct_data(result, original.dtype, original)
    return Series(result)