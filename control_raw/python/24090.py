def state(name, path=None):
    '''
    Returns the state of a container.

    path
        path to the container parent directory (default: /var/lib/lxc)

        .. versionadded:: 2015.8.0

    CLI Example:

    .. code-block:: bash

        salt '*' lxc.state name
    '''
    # Don't use _ensure_exists() here, it will mess with _change_state()

    cachekey = 'lxc.state.{0}{1}'.format(name, path)
    try:
        return __context__[cachekey]
    except KeyError:
        if not exists(name, path=path):
            __context__[cachekey] = None
        else:
            cmd = 'lxc-info'
            if path:
                cmd += ' -P {0}'.format(pipes.quote(path))
            cmd += ' -n {0}'.format(name)
            ret = __salt__['cmd.run_all'](cmd, python_shell=False)
            if ret['retcode'] != 0:
                _clear_context()
                raise CommandExecutionError(
                    'Unable to get state of container \'{0}\''.format(name)
                )
            c_infos = ret['stdout'].splitlines()
            c_state = None
            for c_info in c_infos:
                stat = c_info.split(':')
                if stat[0].lower() == 'state':
                    c_state = stat[1].strip().lower()
                    break
            __context__[cachekey] = c_state
    return __context__[cachekey]