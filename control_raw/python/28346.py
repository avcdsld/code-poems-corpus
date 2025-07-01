def status(cwd, opts=None, user=None):
    '''
    Show changed files of the given repository

    cwd
        The path to the Mercurial repository

    opts : None
        Any additional options to add to the command line

    user : None
        Run hg as a user other than what the minion runs as

    CLI Example:

    .. code-block:: bash

        salt '*' hg.status /path/to/repo
    '''
    def _status(cwd):
        cmd = ['hg', 'status']
        if opts:
            for opt in opts.split():
                cmd.append('{0}'.format(opt))
        out = __salt__['cmd.run_stdout'](
            cmd, cwd=cwd, runas=user, python_shell=False)
        types = {
            'M': 'modified',
            'A': 'added',
            'R': 'removed',
            'C': 'clean',
            '!': 'missing',
            '?': 'not tracked',
            'I': 'ignored',
            ' ': 'origin of the previous file',
        }
        ret = {}
        for line in out.splitlines():
            t, f = types[line[0]], line[2:]
            if t not in ret:
                ret[t] = []
            ret[t].append(f)
        return ret

    if salt.utils.data.is_iter(cwd):
        return dict((cwd, _status(cwd)) for cwd in cwd)
    else:
        return _status(cwd)