def available(name):
    '''
    .. versionadded:: 2014.7.0

    Returns ``True`` if the specified service is available, otherwise returns
    ``False``.

    CLI Example:

    .. code-block:: bash

        salt '*' service.available sshd
    '''
    path = '/etc/rc.d/{0}'.format(name)
    return os.path.isfile(path) and os.access(path, os.X_OK)