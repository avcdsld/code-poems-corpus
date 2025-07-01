def chfullname(name, fullname):
    '''
    Change the user's Full Name

    CLI Example:

    .. code-block:: bash

        salt '*' user.chfullname foo 'Foo Bar'
    '''
    fullname = salt.utils.data.decode(fullname)
    pre_info = info(name)
    if not pre_info:
        raise CommandExecutionError('User \'{0}\' does not exist'.format(name))
    pre_info['fullname'] = salt.utils.data.decode(pre_info['fullname'])
    if fullname == pre_info['fullname']:
        return True
    _dscl(
        ['/Users/{0}'.format(name), 'RealName', fullname],
        # use a 'create' command, because a 'change' command would fail if
        # current fullname is an empty string. The 'create' will just overwrite
        # this field.
        ctype='create'
    )
    # dscl buffers changes, sleep 1 second before checking if new value
    # matches desired value
    time.sleep(1)

    current = salt.utils.data.decode(info(name).get('fullname'))
    return current == fullname