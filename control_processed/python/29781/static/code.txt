def servermods():
    '''
    Return list of modules compiled into the server (``apachectl -l``)

    CLI Example:

    .. code-block:: bash

        salt '*' apache.servermods
    '''
    cmd = '{0} -l'.format(_detect_os())
    ret = []
    out = __salt__['cmd.run'](cmd).splitlines()
    for line in out:
        if not line:
            continue
        if '.c' in line:
            ret.append(line.strip())
    return ret