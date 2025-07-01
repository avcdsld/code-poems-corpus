def from_pystr_to_cstr(data):
    """Convert a list of Python str to C pointer

    Parameters
    ----------
    data : list
        list of str
    """

    if not isinstance(data, list):
        raise NotImplementedError
    pointers = (ctypes.c_char_p * len(data))()
    if PY3:
        data = [bytes(d, 'utf-8') for d in data]
    else:
        data = [d.encode('utf-8') if isinstance(d, unicode) else d  # pylint: disable=undefined-variable
                for d in data]
    pointers[:] = data
    return pointers