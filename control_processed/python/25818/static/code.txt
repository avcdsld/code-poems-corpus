def _linux_disks():
    '''
    Return list of disk devices and work out if they are SSD or HDD.
    '''
    ret = {'disks': [], 'SSDs': []}

    for entry in glob.glob('/sys/block/*/queue/rotational'):
        try:
            with salt.utils.files.fopen(entry) as entry_fp:
                device = entry.split('/')[3]
                flag = entry_fp.read(1)
                if flag == '0':
                    ret['SSDs'].append(device)
                    log.trace('Device %s reports itself as an SSD', device)
                elif flag == '1':
                    ret['disks'].append(device)
                    log.trace('Device %s reports itself as an HDD', device)
                else:
                    log.trace(
                        'Unable to identify device %s as an SSD or HDD. It does '
                        'not report 0 or 1', device
                    )
        except IOError:
            pass
    return ret