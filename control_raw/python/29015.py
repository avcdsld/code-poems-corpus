def get_uid(path, follow_symlinks=True):
    '''
    Return the id of the user that owns a given file

    Symlinks are followed by default to mimic Unix behavior. Specify
    `follow_symlinks=False` to turn off this behavior.

    Args:
        path (str): The path to the file or directory

        follow_symlinks (bool):
            If the object specified by ``path`` is a symlink, get attributes of
            the linked file instead of the symlink itself. Default is True

    Returns:
        str: The uid of the owner


    CLI Example:

    .. code-block:: bash

        salt '*' file.get_uid c:\\temp\\test.txt
        salt '*' file.get_uid c:\\temp\\test.txt follow_symlinks=False
    '''
    if not os.path.exists(path):
        raise CommandExecutionError('Path not found: {0}'.format(path))

    # Under Windows, if the path is a symlink, the user that owns the symlink is
    # returned, not the user that owns the file/directory the symlink is
    # pointing to. This behavior is *different* to *nix, therefore the symlink
    # is first resolved manually if necessary. Remember symlinks are only
    # supported on Windows Vista or later.
    if follow_symlinks and sys.getwindowsversion().major >= 6:
        path = _resolve_symlink(path)

    owner_sid = salt.utils.win_dacl.get_owner(path)
    return salt.utils.win_dacl.get_sid_string(owner_sid)