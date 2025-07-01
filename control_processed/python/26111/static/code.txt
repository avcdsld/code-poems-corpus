def reread(user=None, conf_file=None, bin_env=None):
    '''
    Reload the daemon's configuration files

    user
        user to run supervisorctl as
    conf_file
        path to supervisord config file
    bin_env
        path to supervisorctl bin or path to virtualenv with supervisor
        installed

    CLI Example:

    .. code-block:: bash

        salt '*' supervisord.reread
    '''
    ret = __salt__['cmd.run_all'](
        _ctl_cmd('reread', None, conf_file, bin_env),
        runas=user,
        python_shell=False,
    )
    return _get_return(ret)