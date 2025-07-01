def set_proxy_win(server, port, types=None, bypass_hosts=None):
    '''
    Sets the http proxy settings, only works with Windows.

    server
        The proxy server to use

    password
        The password to use if required by the server

    types
        The types of proxy connections should be setup with this server. Valid
        types are:

            - ``http``
            - ``https``
            - ``ftp``

    bypass_hosts
        The hosts that are allowed to by pass the proxy.

    CLI Example:

    .. code-block:: bash

        salt '*' proxy.set_http_proxy example.com 1080 types="['http', 'https']"
    '''
    if __grains__['os'] == 'Windows':
        return _set_proxy_windows(server=server,
                                  port=port,
                                  types=types,
                                  bypass_hosts=bypass_hosts)