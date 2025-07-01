def activate(name, path, user):
    '''
    Activate a wordpress plugin

    name
        Wordpress plugin name

    path
        path to wordpress install location

    user
        user to run the command as

    CLI Example:

    .. code-block:: bash

        salt '*' wordpress.activate HyperDB /var/www/html apache
    '''
    check = show_plugin(name, path, user)
    if check['status'] == 'active':
        # already active
        return None
    resp = __salt__['cmd.shell']((
        'wp --path={0} plugin activate {1}'
    ).format(path, name), runas=user)
    if 'Success' in resp:
        return True
    elif show_plugin(name, path, user)['status'] == 'active':
        return True
    return False