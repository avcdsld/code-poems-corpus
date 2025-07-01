def add(name, device):
    '''
    Add new device to RAID array.

    CLI Example:

    .. code-block:: bash

        salt '*' raid.add /dev/md0 /dev/sda1

    '''

    cmd = 'mdadm --manage {0} --add {1}'.format(name, device)
    if __salt__['cmd.retcode'](cmd) == 0:
        return True
    return False