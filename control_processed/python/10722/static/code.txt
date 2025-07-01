def coerce_to_dtype(dtype, value):
    """
    Make a value with the specified numpy dtype.

    Only datetime64[ns] and datetime64[D] are supported for datetime dtypes.
    """
    name = dtype.name
    if name.startswith('datetime64'):
        if name == 'datetime64[D]':
            return make_datetime64D(value)
        elif name == 'datetime64[ns]':
            return make_datetime64ns(value)
        else:
            raise TypeError(
                "Don't know how to coerce values of dtype %s" % dtype
            )
    return dtype.type(value)