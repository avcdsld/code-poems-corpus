def enabled(name, **kwargs):
    '''
    Return True if the named service is enabled, false otherwise

    name
        Service name

    .. versionchanged:: 2016.3.4

    Support for jail (representing jid or jail name) keyword argument in kwargs

    CLI Example:

    .. code-block:: bash

        salt '*' service.enabled <service name>
    '''
    jail = kwargs.get('jail', '')
    if not available(name, jail):
        log.error('Service %s not found', name)
        return False

    cmd = '{0} {1} rcvar'.format(_cmd(jail), name)

    for line in __salt__['cmd.run_stdout'](cmd, python_shell=False).splitlines():
        if '_enable="' not in line:
            continue
        _, state, _ = line.split('"', 2)
        return state.lower() in ('yes', 'true', 'on', '1')

    # probably will never reached
    return False