def get_group(path, follow_symlinks=True):
    '''
    Return the group that owns a given file

    path
        file or directory of which to get the group

    follow_symlinks
        indicated if symlinks should be followed

    CLI Example:

    .. code-block:: bash

        salt '*' file.get_group /etc/passwd

    .. versionchanged:: 0.16.4
        ``follow_symlinks`` option added
    '''
    return stats(os.path.expanduser(path), follow_symlinks=follow_symlinks).get('group', False)