def _get_userprofile_from_registry(user, sid):
    '''
    In case net user doesn't return the userprofile we can get it from the
    registry

    Args:
        user (str): The user name, used in debug message

        sid (str): The sid to lookup in the registry

    Returns:
        str: Profile directory
    '''
    profile_dir = __utils__['reg.read_value'](
        'HKEY_LOCAL_MACHINE',
        'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\{0}'.format(sid),
        'ProfileImagePath'
    )['vdata']
    log.debug(
        'user %s with sid=%s profile is located at "%s"',
        user, sid, profile_dir
    )
    return profile_dir