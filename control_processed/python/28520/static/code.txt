def add(name, gid=None, **kwargs):
    '''
    Add the specified group

    CLI Example:

    .. code-block:: bash

        salt '*' group.add foo 3456
    '''
    kwargs = salt.utils.args.clean_kwargs(**kwargs)
    if salt.utils.data.is_true(kwargs.pop('system', False)):
        log.warning('pw_group module does not support the \'system\' argument')
    if kwargs:
        log.warning('Invalid kwargs passed to group.add')

    cmd = 'pw groupadd '
    if gid:
        cmd += '-g {0} '.format(gid)
    cmd = '{0} -n {1}'.format(cmd, name)
    ret = __salt__['cmd.run_all'](cmd, python_shell=False)

    return not ret['retcode']