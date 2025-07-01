def vms(nictag):
    '''
    List all vms connect to nictag

    nictag : string
        name of nictag

    CLI Example:

    .. code-block:: bash

        salt '*' nictagadm.vms admin
    '''
    ret = {}
    cmd = 'nictagadm vms {0}'.format(nictag)
    res = __salt__['cmd.run_all'](cmd)
    retcode = res['retcode']
    if retcode != 0:
        ret['Error'] = res['stderr'] if 'stderr' in res else 'Failed to get list of vms.'
    else:
        ret = res['stdout'].splitlines()
    return ret