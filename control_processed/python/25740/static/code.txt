def file_list(*packages, **kwargs):
    '''
    List the files that belong to a package. Not specifying any packages will
    return a list of _every_ file on the system's package database (not
    generally recommended).

    CLI Examples:

    .. code-block:: bash

        salt '*' lowpkg.file_list httpd
        salt '*' lowpkg.file_list httpd postfix
        salt '*' lowpkg.file_list
    '''
    errors = []
    ret = set([])
    pkgs = {}
    cmd = 'dpkg -l {0}'.format(' '.join(packages))
    out = __salt__['cmd.run_all'](cmd, python_shell=False)
    if out['retcode'] != 0:
        msg = 'Error:  ' + out['stderr']
        log.error(msg)
        return msg
    out = out['stdout']

    for line in out.splitlines():
        if line.startswith('ii '):
            comps = line.split()
            pkgs[comps[1]] = {'version': comps[2],
                              'description': ' '.join(comps[3:])}
        if 'No packages found' in line:
            errors.append(line)
    for pkg in pkgs:
        files = []
        cmd = 'dpkg -L {0}'.format(pkg)
        for line in __salt__['cmd.run'](cmd, python_shell=False).splitlines():
            files.append(line)
        fileset = set(files)
        ret = ret.union(fileset)
    return {'errors': errors, 'files': list(ret)}