def state(name):
    '''
    Return state of container (running or stopped)

    CLI Example:

    .. code-block:: bash

        salt myminion nspawn.state <name>
    '''
    try:
        cmd = 'show {0} --property=State'.format(name)
        return _machinectl(cmd, ignore_retcode=True)['stdout'].split('=')[-1]
    except IndexError:
        return 'stopped'