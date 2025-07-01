def attachable(name, path=None):
    '''
    Return True if the named container can be attached to via the lxc-attach
    command

    path
        path to the container parent
        default: /var/lib/lxc (system default)

        .. versionadded:: 2015.8.0

    CLI Example:

    .. code-block:: bash

        salt 'minion' lxc.attachable ubuntu
    '''
    cachekey = 'lxc.attachable{0}{1}'.format(name, path)
    try:
        return __context__[cachekey]
    except KeyError:
        _ensure_exists(name, path=path)
        # Can't use run() here because it uses attachable() and would
        # endlessly recurse, resulting in a traceback
        log.debug('Checking if LXC container %s is attachable', name)
        cmd = 'lxc-attach'
        if path:
            cmd += ' -P {0}'.format(pipes.quote(path))
        cmd += ' --clear-env -n {0} -- /usr/bin/env'.format(name)
        result = __salt__['cmd.retcode'](cmd,
                                         python_shell=False,
                                         output_loglevel='quiet',
                                         ignore_retcode=True) == 0
        __context__[cachekey] = result
    return __context__[cachekey]