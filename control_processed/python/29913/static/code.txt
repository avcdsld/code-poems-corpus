def _ppid():
    '''
    Return a dict of pid to ppid mappings
    '''
    ret = {}
    if __grains__['kernel'] == 'SunOS':
        cmd = 'ps -a -o pid,ppid | tail +2'
    else:
        cmd = 'ps -ax -o pid,ppid | tail -n+2'
    out = __salt__['cmd.run'](cmd, python_shell=True)
    for line in out.splitlines():
        pid, ppid = line.split()
        ret[pid] = ppid
    return ret