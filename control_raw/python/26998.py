def refresh_db(root=None, **kwargs):
    '''
    Just run a ``pacman -Sy``, return a dict::

        {'<database name>': Bool}

    CLI Example:

    .. code-block:: bash

        salt '*' pkg.refresh_db
    '''
    # Remove rtag file to keep multiple refreshes from happening in pkg states
    salt.utils.pkg.clear_rtag(__opts__)
    cmd = ['pacman', '-Sy']

    if root is not None:
        cmd.extend(('-r', root))

    ret = {}
    call = __salt__['cmd.run_all'](cmd,
                                   output_loglevel='trace',
                                   env={'LANG': 'C'},
                                   python_shell=False)
    if call['retcode'] != 0:
        comment = ''
        if 'stderr' in call:
            comment += ': ' + call['stderr']
        raise CommandExecutionError(
            'Error refreshing package database' + comment
        )
    else:
        out = call['stdout']

    for line in salt.utils.itertools.split(out, '\n'):
        if line.strip().startswith('::'):
            continue
        if not line:
            continue
        key = line.strip().split()[0]
        if 'is up to date' in line:
            ret[key] = False
        elif 'downloading' in line:
            key = line.strip().split()[1].split('.')[0]
            ret[key] = True
    return ret