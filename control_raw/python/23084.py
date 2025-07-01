def disconnect_session(session_id):
    '''
    Disconnect a session.

    .. versionadded:: 2016.11.0

    :param session_id: The numeric Id of the session.
    :return: A boolean representing whether the disconnect succeeded.

    CLI Example:

    .. code-block:: bash

        salt '*' rdp.disconnect_session session_id

        salt '*' rdp.disconnect_session 99
    '''
    try:
        win32ts.WTSDisconnectSession(win32ts.WTS_CURRENT_SERVER_HANDLE, session_id, True)
    except PyWinError as error:
        _LOG.error('Error calling WTSDisconnectSession: %s', error)
        return False
    return True