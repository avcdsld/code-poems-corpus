def server_enabled(s_name, **connection_args):
    '''
    Check if a server is enabled globally

    CLI Example:

    .. code-block:: bash

        salt '*' netscaler.server_enabled 'serverName'
    '''
    server = _server_get(s_name, **connection_args)
    return server is not None and server.get_state() == 'ENABLED'