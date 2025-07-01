def unpackb(packed, **kwargs):
    '''
    .. versionadded:: 2018.3.4

    Wraps msgpack.unpack.

    By default, this function uses the msgpack module and falls back to
    msgpack_pure, if the msgpack is not available. You can pass an alternate
    msgpack module using the _msgpack_module argument.
    '''
    msgpack_module = kwargs.pop('_msgpack_module', msgpack)
    return msgpack_module.unpackb(packed, **kwargs)