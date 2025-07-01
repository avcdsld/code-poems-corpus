def install(name, link, path, priority):
    '''
    Install symbolic links determining default commands

    CLI Example:

    .. code-block:: bash

        salt '*' alternatives.install editor /usr/bin/editor /usr/bin/emacs23 50
    '''
    cmd = [_get_cmd(), '--install', link, name, path, six.text_type(priority)]
    out = __salt__['cmd.run_all'](cmd, python_shell=False)
    if out['retcode'] > 0 and out['stderr'] != '':
        return out['stderr']
    return out['stdout']