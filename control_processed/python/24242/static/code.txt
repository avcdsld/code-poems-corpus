def get_default_group(user):
    '''
    Returns the specified user's default group. If the user doesn't exist, a
    KeyError will be raised.
    '''
    return grp.getgrgid(pwd.getpwnam(user).pw_gid).gr_name \
        if HAS_GRP and HAS_PWD \
        else None