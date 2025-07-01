def stop(vm, force=False, key='uuid'):
    '''
    Stop a vm

    vm : string
        vm to be stopped
    force : boolean
        force stop of vm if true
    key : string [uuid|alias|hostname]
        value type of 'vm' parameter

    CLI Example:

    .. code-block:: bash

        salt '*' vmadm.stop 186da9ab-7392-4f55-91a5-b8f1fe770543
        salt '*' vmadm.stop 186da9ab-7392-4f55-91a5-b8f1fe770543 True
        salt '*' vmadm.stop vm=nacl key=alias
        salt '*' vmadm.stop vm=nina.example.org key=hostname
    '''
    ret = {}
    if key not in ['uuid', 'alias', 'hostname']:
        ret['Error'] = 'Key must be either uuid, alias or hostname'
        return ret
    vm = lookup('{0}={1}'.format(key, vm), one=True)
    if 'Error' in vm:
        return vm
    # vmadm stop <uuid> [-F]
    cmd = 'vmadm stop {force} {uuid}'.format(
        force='-F' if force else '',
        uuid=vm
    )
    res = __salt__['cmd.run_all'](cmd)
    retcode = res['retcode']
    if retcode != 0:
        ret['Error'] = _exit_status(retcode)
        return ret
    return True