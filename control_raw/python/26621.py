def __csf_cmd(cmd):
    '''
    Execute csf command
    '''
    csf_cmd = '{0} {1}'.format(salt.utils.path.which('csf'), cmd)
    out = __salt__['cmd.run_all'](csf_cmd)

    if out['retcode'] != 0:
        if not out['stderr']:
            ret = out['stdout']
        else:
            ret = out['stderr']
        raise CommandExecutionError(
            'csf failed: {0}'.format(ret)
        )
    else:
        ret = out['stdout']
    return ret