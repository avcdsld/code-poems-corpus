def _dtype_to_default_stata_fmt(dtype, column, dta_version=114,
                                force_strl=False):
    """
    Map numpy dtype to stata's default format for this type. Not terribly
    important since users can change this in Stata. Semantics are

    object  -> "%DDs" where DD is the length of the string.  If not a string,
                raise ValueError
    float64 -> "%10.0g"
    float32 -> "%9.0g"
    int64   -> "%9.0g"
    int32   -> "%12.0g"
    int16   -> "%8.0g"
    int8    -> "%8.0g"
    strl    -> "%9s"
    """
    # TODO: Refactor to combine type with format
    # TODO: expand this to handle a default datetime format?
    if dta_version < 117:
        max_str_len = 244
    else:
        max_str_len = 2045
        if force_strl:
            return '%9s'
    if dtype.type == np.object_:
        inferred_dtype = infer_dtype(column, skipna=True)
        if not (inferred_dtype in ('string', 'unicode') or
                len(column) == 0):
            raise ValueError('Column `{col}` cannot be exported.\n\nOnly '
                             'string-like object arrays containing all '
                             'strings or a mix of strings and None can be '
                             'exported. Object arrays containing only null '
                             'values are prohibited. Other object types'
                             'cannot be exported and must first be converted '
                             'to one of the supported '
                             'types.'.format(col=column.name))
        itemsize = max_len_string_array(ensure_object(column.values))
        if itemsize > max_str_len:
            if dta_version >= 117:
                return '%9s'
            else:
                raise ValueError(excessive_string_length_error % column.name)
        return "%" + str(max(itemsize, 1)) + "s"
    elif dtype == np.float64:
        return "%10.0g"
    elif dtype == np.float32:
        return "%9.0g"
    elif dtype == np.int32:
        return "%12.0g"
    elif dtype == np.int8 or dtype == np.int16:
        return "%8.0g"
    else:  # pragma : no cover
        raise NotImplementedError(
            "Data type {dtype} not supported.".format(dtype=dtype))