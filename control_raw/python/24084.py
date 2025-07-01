def start(name, **kwargs):
    '''
    Start the named container

    path
        path to the container parent directory
        default: /var/lib/lxc (system)

        .. versionadded:: 2015.8.0

    lxc_config
        path to a lxc config file
        config file will be guessed from container name otherwise

        .. versionadded:: 2015.8.0

    use_vt
        run the command through VT

        .. versionadded:: 2015.8.0

    CLI Example:

    .. code-block:: bash

        salt myminion lxc.start name
    '''
    path = kwargs.get('path', None)
    cpath = get_root_path(path)
    lxc_config = kwargs.get('lxc_config', None)
    cmd = 'lxc-start'
    if not lxc_config:
        lxc_config = os.path.join(cpath, name, 'config')
    # we try to start, even without config, if global opts are there
    if os.path.exists(lxc_config):
        cmd += ' -f {0}'.format(pipes.quote(lxc_config))
    cmd += ' -d'
    _ensure_exists(name, path=path)
    if state(name, path=path) == 'frozen':
        raise CommandExecutionError(
            'Container \'{0}\' is frozen, use lxc.unfreeze'.format(name)
        )
    # lxc-start daemonize itself violently, we must not communicate with it
    use_vt = kwargs.get('use_vt', None)
    with_communicate = kwargs.get('with_communicate', False)
    return _change_state(cmd, name, 'running',
                         stdout=None,
                         stderr=None,
                         stdin=None,
                         with_communicate=with_communicate,
                         path=path,
                         use_vt=use_vt)