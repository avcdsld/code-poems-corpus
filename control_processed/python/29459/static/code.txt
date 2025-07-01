def set_binary_path(name):
    '''
    Sets the path, where the syslog-ng binary can be found. This function is
    intended to be used from states.

    If syslog-ng is installed via a package manager, users don't need to use
    this function.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.set_binary_path name=/usr/sbin

    '''
    global __SYSLOG_NG_BINARY_PATH
    old = __SYSLOG_NG_BINARY_PATH
    __SYSLOG_NG_BINARY_PATH = name
    changes = _format_changes(old, name)
    return _format_state_result(name, result=True, changes=changes)