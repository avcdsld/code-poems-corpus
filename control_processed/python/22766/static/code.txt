def config_get(pattern='*', host=None, port=None, db=None, password=None):
    '''
    Get redis server configuration values

    CLI Example:

    .. code-block:: bash

        salt '*' redis.config_get
        salt '*' redis.config_get port
    '''
    server = _connect(host, port, db, password)
    return server.config_get(pattern)