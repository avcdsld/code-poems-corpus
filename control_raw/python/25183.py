def del_password(name, root=None):
    '''
    .. versionadded:: 2014.7.0

    Delete the password from name user

    name
        User to delete

    root
        Directory to chroot into

    CLI Example:

    .. code-block:: bash

        salt '*' shadow.del_password username
    '''
    cmd = ['passwd']
    if root is not None:
        cmd.extend(('-R', root))
    cmd.extend(('-d', name))

    __salt__['cmd.run'](cmd, python_shell=False, output_loglevel='quiet')
    uinfo = info(name, root=root)
    return not uinfo['passwd'] and uinfo['name'] == name