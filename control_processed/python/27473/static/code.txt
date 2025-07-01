def mkfs(device, fs_type):
    '''
    Makes a file system <fs_type> on partition <device>, destroying all data
    that resides on that partition. <fs_type> must be one of "ext2", "fat32",
    "fat16", "linux-swap" or "reiserfs" (if libreiserfs is installed)

    CLI Example:

    .. code-block:: bash

        salt '*' partition.mkfs /dev/sda2 fat32
    '''
    _validate_device(device)

    if not _is_fstype(fs_type):
        raise CommandExecutionError('Invalid fs_type passed to partition.mkfs')

    if fs_type == 'NTFS':
        fs_type = 'ntfs'

    if fs_type == 'linux-swap':
        mkfs_cmd = 'mkswap'
    else:
        mkfs_cmd = 'mkfs.{0}'.format(fs_type)

    if not salt.utils.path.which(mkfs_cmd):
        return 'Error: {0} is unavailable.'.format(mkfs_cmd)
    cmd = '{0} {1}'.format(mkfs_cmd, device)
    out = __salt__['cmd.run'](cmd).splitlines()
    return out