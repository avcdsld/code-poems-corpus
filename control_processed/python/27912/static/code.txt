def send(vm, target, key='uuid'):
    '''
    Send a vm to a directory

    vm : string
        vm to be sent
    target : string
        target directory
    key : string [uuid|alias|hostname]
        value type of 'vm' parameter

    CLI Example:

    .. code-block:: bash

        salt '*' vmadm.send 186da9ab-7392-4f55-91a5-b8f1fe770543 /opt/backups
        salt '*' vmadm.send vm=nacl target=/opt/backups key=alias
    '''
    ret = {}
    if key not in ['uuid', 'alias', 'hostname']:
        ret['Error'] = 'Key must be either uuid, alias or hostname'
        return ret
    if not os.path.isdir(target):
        ret['Error'] = 'Target must be a directory or host'
        return ret
    vm = lookup('{0}={1}'.format(key, vm), one=True)
    if 'Error' in vm:
        return vm
    # vmadm send <uuid> [target]
    cmd = 'vmadm send {uuid} > {target}'.format(
        uuid=vm,
        target=os.path.join(target, '{0}.vmdata'.format(vm))
    )
    res = __salt__['cmd.run_all'](cmd, python_shell=True)
    retcode = res['retcode']
    if retcode != 0:
        ret['Error'] = res['stderr'] if 'stderr' in res else _exit_status(retcode)
        return ret
    vmobj = get(vm)
    if 'datasets' not in vmobj:
        return True
    log.warning('one or more datasets detected, this is not supported!')
    log.warning('trying to zfs send datasets...')
    for dataset in vmobj['datasets']:
        name = dataset.split('/')
        name = name[-1]
        cmd = 'zfs send {dataset} > {target}'.format(
            dataset=dataset,
            target=os.path.join(target, '{0}-{1}.zfsds'.format(vm, name))
        )
        res = __salt__['cmd.run_all'](cmd, python_shell=True)
        retcode = res['retcode']
        if retcode != 0:
            ret['Error'] = res['stderr'] if 'stderr' in res else _exit_status(retcode)
            return ret
    return True