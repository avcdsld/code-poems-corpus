def cast_vdata(vdata=None, vtype='REG_SZ'):
    '''
    Cast the ``vdata` value to the appropriate data type for the registry type
    specified in ``vtype``

    Args:

        vdata (str, int, list, bytes): The data to cast

        vtype (str):
            The type of data to be written to the registry. Must be one of the
            following:

                - REG_BINARY
                - REG_DWORD
                - REG_EXPAND_SZ
                - REG_MULTI_SZ
                - REG_QWORD
                - REG_SZ

    Returns:
        The vdata cast to the appropriate type. Will be unicode string, binary,
        list of unicode strings, or int

    Usage:

        .. code-block:: python

            import salt.utils.win_reg
            winreg.cast_vdata(vdata='This is the string', vtype='REG_SZ')
    '''
    # Check data type and cast to expected type
    # int will automatically become long on 64bit numbers
    # https://www.python.org/dev/peps/pep-0237/

    registry = Registry()
    vtype_value = registry.vtype[vtype]

    # String Types to Unicode
    if vtype_value in [win32con.REG_SZ, win32con.REG_EXPAND_SZ]:
        return _to_unicode(vdata)
    # Don't touch binary... if it's binary
    elif vtype_value == win32con.REG_BINARY:
        if isinstance(vdata, six.text_type):
            # Unicode data must be encoded
            return vdata.encode('utf-8')
        return vdata
    # Make sure REG_MULTI_SZ is a list of strings
    elif vtype_value == win32con.REG_MULTI_SZ:
        return [_to_unicode(i) for i in vdata]
    # Make sure REG_QWORD is a 64 bit integer
    elif vtype_value == win32con.REG_QWORD:
        return vdata if six.PY3 else long(vdata)  # pylint: disable=incompatible-py3-code,undefined-variable
    # Everything else is int
    else:
        return int(vdata)