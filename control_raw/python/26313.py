def chgid(name, gid):
    '''
    Change the default group of the user

    CLI Example:

    .. code-block:: bash

        salt '*' user.chgid foo 4376
    '''
    if not isinstance(gid, int):
        raise SaltInvocationError('gid must be an integer')
    pre_info = info(name)
    if not pre_info:
        raise CommandExecutionError('User \'{0}\' does not exist'.format(name))
    if gid == pre_info['gid']:
        return True
    _dscl(
        ['/Users/{0}'.format(name), 'PrimaryGroupID', pre_info['gid'], gid],
        ctype='change'
    )
    # dscl buffers changes, sleep 1 second before checking if new value
    # matches desired value
    time.sleep(1)
    return info(name).get('gid') == gid