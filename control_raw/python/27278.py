def deluser(name, username, root=None):
    '''
    Remove a user from the group.

    name
        Name of the group to modify

    username
        Username to delete from the group

    root
        Directory to chroot into

    CLI Example:

    .. code-block:: bash

         salt '*' group.deluser foo bar

    Removes a member user 'bar' from a group 'foo'. If group is not present
    then returns True.
    '''
    on_redhat_5 = __grains__.get('os_family') == 'RedHat' and __grains__.get('osmajorrelease') == '5'
    on_suse_11 = __grains__.get('os_family') == 'Suse' and __grains__.get('osmajorrelease') == '11'

    grp_info = __salt__['group.info'](name)
    try:
        if username in grp_info['members']:
            if __grains__['kernel'] == 'Linux':
                if on_redhat_5:
                    cmd = ['gpasswd', '-d', username, name]
                elif on_suse_11:
                    cmd = ['usermod', '-R', name, username]
                else:
                    cmd = ['gpasswd', '--del', username, name]
                if root is not None:
                    cmd.extend(('--root', root))
                retcode = __salt__['cmd.retcode'](cmd, python_shell=False)
            elif __grains__['kernel'] == 'OpenBSD':
                out = __salt__['cmd.run_stdout']('id -Gn {0}'.format(username),
                                                 python_shell=False)
                cmd = ['usermod', '-S']
                cmd.append(','.join([g for g in out.split() if g != six.text_type(name)]))
                cmd.append('{0}'.format(username))
                retcode = __salt__['cmd.retcode'](cmd, python_shell=False)
            else:
                log.error('group.deluser is not yet supported on this platform')
                return False
            return not retcode
        else:
            return True
    except Exception:
        return True