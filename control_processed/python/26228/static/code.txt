def subvolume_set_default(subvolid, path):
    '''
    Set the subvolume as default

    subvolid
        ID of the new default subvolume

    path
        Mount point for the filesystem

    CLI Example:

    .. code-block:: bash

        salt '*' btrfs.subvolume_set_default 257 /var/volumes/tmp

    '''
    cmd = ['btrfs', 'subvolume', 'set-default', subvolid, path]

    res = __salt__['cmd.run_all'](cmd)
    salt.utils.fsutils._verify_run(res)
    return True