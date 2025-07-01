def get_x():
    '''
    Get current X keyboard setting

    CLI Example:

    .. code-block:: bash

        salt '*' keyboard.get_x
    '''
    cmd = 'setxkbmap -query | grep layout'
    out = __salt__['cmd.run'](cmd, python_shell=True).split(':')
    return out[1].strip()