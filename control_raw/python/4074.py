def establish_ssh(target=None, auto_trust=False, allow_agent=True, look_keys=True):
    r'''
    Establish a SSH connection to a remote host. It should be able to use
    SSH's config file Host name declarations. By default, will not automatically
    add trust for hosts, will use SSH agent and will try to load keys.
    '''

    def password_prompt(username, hostname):
        r'''
        If the Host is relying on password authentication, lets ask it.
        Relying on SSH itself to take care of that would not work when the
        remote authentication is password behind a SSH-key+2FA jumphost.
        '''
        return getpass.getpass('No SSH key for %s@%s, please provide password: ' % (username, hostname))

    ssh_conn = None
    if target is not None:
        ssh_conf = get_sshconfig()
        cfg = {
            'hostname': None,
            'port': 22,
            'allow_agent': allow_agent,
            'look_for_keys': look_keys
        }
        if ssh_conf.has_key(target):
            user_config = ssh_conf.get(target)

            # If ssh_config file's Host defined 'User' instead of 'Username'
            if user_config.has_key('user') and not user_config.has_key('username'):
                user_config['username'] = user_config['user']
                del user_config['user']

            for k in ('username', 'hostname', 'port'):
                if k in user_config:
                    cfg[k] = user_config[k]

            # Assume Password auth. If we don't do that, then when connecting
            # through a jumphost we will run into issues and the user will
            # not be able to input his password to the SSH prompt.
            if 'identityfile' in user_config:
                cfg['key_filename'] = user_config['identityfile']
            else:
                cfg['password'] = password_prompt(cfg['username'], cfg['hostname'] or target)

            # Should be the last one, since ProxyCommand will issue connection to remote host
            if 'proxycommand' in user_config:
                cfg['sock'] = paramiko.ProxyCommand(user_config['proxycommand'])

        else:
            cfg['username'] = target.split('@')[0]
            cfg['hostname'] = target.split('@')[1].split(':')[0]
            cfg['password'] = password_prompt(cfg['username'], cfg['hostname'])
            try:
                cfg['port'] = int(target.split('@')[1].split(':')[1])
            except IndexError:
                # IndexError will happen if no :PORT is there.
                # Default value 22 is defined above in 'cfg'.
                pass

        ssh_conn = paramiko.SSHClient()
        if auto_trust:
            ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_conn.connect(**cfg)

    return ssh_conn