def set_(key,
         value,
         host=DEFAULT_HOST,
         port=DEFAULT_PORT,
         time=DEFAULT_TIME,
         min_compress_len=DEFAULT_MIN_COMPRESS_LEN):
    '''
    Set a key on the memcached server, overwriting the value if it exists.

    CLI Example:

    .. code-block:: bash

        salt '*' memcached.set <key> <value>
    '''
    if not isinstance(time, six.integer_types):
        raise SaltInvocationError('\'time\' must be an integer')
    if not isinstance(min_compress_len, six.integer_types):
        raise SaltInvocationError('\'min_compress_len\' must be an integer')
    conn = _connect(host, port)
    _check_stats(conn)
    return conn.set(key, value, time, min_compress_len)