def _check_symlink_ownership(path, user, group, win_owner):
    '''
    Check if the symlink ownership matches the specified user and group
    '''
    cur_user, cur_group = _get_symlink_ownership(path)
    if salt.utils.platform.is_windows():
        return win_owner == cur_user
    else:
        return (cur_user == user) and (cur_group == group)