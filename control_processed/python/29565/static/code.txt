def fpopen(*args, **kwargs):
    '''
    Shortcut for fopen with extra uid, gid, and mode options.

    Supported optional Keyword Arguments:

    mode
        Explicit mode to set. Mode is anything os.chmod would accept
        as input for mode. Works only on unix/unix-like systems.

    uid
        The uid to set, if not set, or it is None or -1 no changes are
        made. Same applies if the path is already owned by this uid.
        Must be int. Works only on unix/unix-like systems.

    gid
        The gid to set, if not set, or it is None or -1 no changes are
        made. Same applies if the path is already owned by this gid.
        Must be int. Works only on unix/unix-like systems.

    '''
    # Remove uid, gid and mode from kwargs if present
    uid = kwargs.pop('uid', -1)  # -1 means no change to current uid
    gid = kwargs.pop('gid', -1)  # -1 means no change to current gid
    mode = kwargs.pop('mode', None)
    with fopen(*args, **kwargs) as f_handle:
        path = args[0]
        d_stat = os.stat(path)

        if hasattr(os, 'chown'):
            # if uid and gid are both -1 then go ahead with
            # no changes at all
            if (d_stat.st_uid != uid or d_stat.st_gid != gid) and \
                    [i for i in (uid, gid) if i != -1]:
                os.chown(path, uid, gid)

        if mode is not None:
            mode_part = stat.S_IMODE(d_stat.st_mode)
            if mode_part != mode:
                os.chmod(path, (d_stat.st_mode ^ mode_part) | mode)

        yield f_handle