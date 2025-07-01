def dump(device, args=None):
    '''
    Return all contents of dumpe2fs for a specified device

    CLI Example:

    .. code-block:: bash

        salt '*' extfs.dump /dev/sda1
    '''
    cmd = 'dumpe2fs {0}'.format(device)
    if args:
        cmd = cmd + ' -' + args
    ret = {'attributes': {}, 'blocks': {}}
    out = __salt__['cmd.run'](cmd, python_shell=False).splitlines()
    mode = 'opts'
    group = None
    for line in out:
        if not line:
            continue
        if line.startswith('dumpe2fs'):
            continue
        if mode == 'opts':
            line = line.replace('\t', ' ')
            comps = line.split(': ')
            if line.startswith('Filesystem features'):
                ret['attributes'][comps[0]] = comps[1].split()
            elif line.startswith('Group') and not line.startswith('Group descriptor size'):
                mode = 'blocks'
            else:
                if len(comps) < 2:
                    continue
                ret['attributes'][comps[0]] = comps[1].strip()

        if mode == 'blocks':
            if line.startswith('Group'):
                line = line.replace(':', '')
                line = line.replace('(', '')
                line = line.replace(')', '')
                line = line.replace('[', '')
                line = line.replace(']', '')
                comps = line.split()
                blkgrp = comps[1]
                group = 'Group {0}'.format(blkgrp)
                ret['blocks'][group] = {}
                ret['blocks'][group]['group'] = blkgrp
                ret['blocks'][group]['range'] = comps[3]
                # TODO: comps[4:], which may look one one of the following:
                #     ITABLE_ZEROED
                #     INODE_UNINIT, ITABLE_ZEROED
                # Does anyone know what to call these?
                ret['blocks'][group]['extra'] = []
            elif 'Free blocks:' in line:
                comps = line.split(': ')
                free_blocks = comps[1].split(', ')
                ret['blocks'][group]['free blocks'] = free_blocks
            elif 'Free inodes:' in line:
                comps = line.split(': ')
                inodes = comps[1].split(', ')
                ret['blocks'][group]['free inodes'] = inodes
            else:
                line = line.strip()
                ret['blocks'][group]['extra'].append(line)
    return ret