def delete_set(set=None, family='ipv4'):
    '''
    .. versionadded:: 2014.7.0

    Delete ipset set.

    CLI Example:

    .. code-block:: bash

        salt '*' ipset.delete_set custom_set

        IPv6:
        salt '*' ipset.delete_set custom_set family=ipv6
    '''

    if not set:
        return 'Error: Set needs to be specified'

    cmd = '{0} destroy {1}'.format(_ipset_cmd(), set)
    out = __salt__['cmd.run'](cmd, python_shell=False)

    if not out:
        out = True
    return out