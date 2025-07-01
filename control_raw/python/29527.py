def info(dev):
    '''
    Extract all info delivered by udevadm

    CLI Example:

    .. code-block:: bash

        salt '*' udev.info /dev/sda
        salt '*' udev.info /sys/class/net/eth0
    '''
    if 'sys' in dev:
        qtype = 'path'
    else:
        qtype = 'name'

    cmd = 'udevadm info --export --query=all --{0}={1}'.format(qtype, dev)
    udev_result = __salt__['cmd.run_all'](cmd, output_loglevel='quiet')

    if udev_result['retcode'] != 0:
        raise CommandExecutionError(udev_result['stderr'])

    return _parse_udevadm_info(udev_result['stdout'])[0]