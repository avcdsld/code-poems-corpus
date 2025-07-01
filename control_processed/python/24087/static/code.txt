def unfreeze(name, path=None, use_vt=None):
    '''
    Unfreeze the named container.

    path
        path to the container parent directory
        default: /var/lib/lxc (system)

        .. versionadded:: 2015.8.0

    use_vt
        run the command through VT

        .. versionadded:: 2015.8.0

    CLI Example:

    .. code-block:: bash

        salt '*' lxc.unfreeze name
    '''
    _ensure_exists(name, path=path)
    if state(name, path=path) == 'stopped':
        raise CommandExecutionError(
            'Container \'{0}\' is stopped'.format(name)
        )
    cmd = 'lxc-unfreeze'
    if path:
        cmd += ' -P {0}'.format(pipes.quote(path))
    return _change_state(cmd, name, 'running', path=path, use_vt=use_vt)