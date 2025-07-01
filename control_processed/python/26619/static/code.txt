def _temp_exists(method, ip):
    '''
    Checks if the ip exists as a temporary rule based
    on the method supplied, (tempallow, tempdeny).
    '''
    _type = method.replace('temp', '').upper()
    cmd = "csf -t | awk -v code=1 -v type=_type -v ip=ip '$1==type && $2==ip {{code=0}} END {{exit code}}'".format(_type=_type, ip=ip)
    exists = __salt__['cmd.run_all'](cmd)
    return not bool(exists['retcode'])