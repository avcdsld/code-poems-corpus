def disable_auto_login():
    '''
    .. versionadded:: 2016.3.0

    Disables auto login on the machine

    Returns:
        bool: ``True`` if successful, otherwise ``False``

    CLI Example:

    .. code-block:: bash

        salt '*' user.disable_auto_login
    '''
    # Remove the kcpassword file
    cmd = 'rm -f /etc/kcpassword'
    __salt__['cmd.run'](cmd)

    # Remove the entry from the defaults file
    cmd = ['defaults',
           'delete',
           '/Library/Preferences/com.apple.loginwindow.plist',
           'autoLoginUser']
    __salt__['cmd.run'](cmd)
    return True if not get_auto_login() else False