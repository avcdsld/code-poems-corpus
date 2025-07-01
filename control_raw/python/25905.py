def bootstrap(vm_, opts=None):
    '''
    This is the primary entry point for logging into any system (POSIX or
    Windows) to install Salt. It will make the decision on its own as to which
    deploy function to call.
    '''
    if opts is None:
        opts = __opts__
    deploy_config = salt.config.get_cloud_config_value(
        'deploy',
        vm_, opts, default=False)
    inline_script_config = salt.config.get_cloud_config_value(
        'inline_script',
        vm_, opts, default=None)
    if deploy_config is False and inline_script_config is None:
        return {
            'Error': {
                'No Deploy': '\'deploy\' is not enabled. Not deploying.'
            }
        }

    if vm_.get('driver') == 'saltify':
        saltify_driver = True
    else:
        saltify_driver = False

    key_filename = salt.config.get_cloud_config_value(
        'key_filename', vm_, opts, search_global=False,
        default=salt.config.get_cloud_config_value(
            'ssh_keyfile', vm_, opts, search_global=False, default=None
        )
    )
    if key_filename is not None and not os.path.isfile(key_filename):
        raise SaltCloudConfigError(
            'The defined ssh_keyfile \'{0}\' does not exist'.format(
                key_filename
            )
        )
    has_ssh_agent = False
    if (opts.get('ssh_agent', False) and
            'SSH_AUTH_SOCK' in os.environ and
            stat.S_ISSOCK(os.stat(os.environ['SSH_AUTH_SOCK']).st_mode)):
        has_ssh_agent = True

    if (key_filename is None and
            salt.config.get_cloud_config_value(
                'password', vm_, opts, default=None
            ) is None and
            salt.config.get_cloud_config_value(
                'win_password', vm_, opts, default=None
            ) is None and
            has_ssh_agent is False):
        raise SaltCloudSystemExit(
            'Cannot deploy Salt in a VM if the \'key_filename\' setting '
            'is not set and there is no password set for the VM. '
            'Check the provider docs for \'change_password\' option if it '
            'is supported by your provider.'
        )

    ret = {}

    minion_conf = minion_config(opts, vm_)
    deploy_script_code = os_script(
        salt.config.get_cloud_config_value(
            'os', vm_, opts, default='bootstrap-salt'
        ),
        vm_, opts, minion_conf
    )

    ssh_username = salt.config.get_cloud_config_value(
        'ssh_username', vm_, opts, default='root'
    )

    if 'file_transport' not in opts:
        opts['file_transport'] = vm_.get('file_transport', 'sftp')

    # If we haven't generated any keys yet, do so now.
    if 'pub_key' not in vm_ and 'priv_key' not in vm_:
        log.debug('Generating keys for \'%s\'', vm_['name'])

        vm_['priv_key'], vm_['pub_key'] = gen_keys(
            salt.config.get_cloud_config_value(
                'keysize',
                vm_,
                opts
            )
        )

        key_id = vm_.get('name')
        if 'append_domain' in vm_:
            key_id = '.'.join([key_id, vm_['append_domain']])

        accept_key(
            opts['pki_dir'], vm_['pub_key'], key_id
        )

    if 'os' not in vm_:
        vm_['os'] = salt.config.get_cloud_config_value(
            'script',
            vm_,
            opts
        )

    # NOTE: deploy_kwargs is also used to pass inline_script variable content
    #       to run_inline_script function
    host = salt.config.get_cloud_config_value('ssh_host', vm_, opts)
    deploy_kwargs = {
        'opts': opts,
        'host': host,
        'port': salt.config.get_cloud_config_value(
            'ssh_port', vm_, opts, default=22
        ),
        'salt_host': vm_.get('salt_host', host),
        'username': ssh_username,
        'script': deploy_script_code,
        'inline_script': inline_script_config,
        'name': vm_['name'],
        'has_ssh_agent': has_ssh_agent,
        'tmp_dir': salt.config.get_cloud_config_value(
            'tmp_dir', vm_, opts, default='/tmp/.saltcloud'
        ),
        'vm_': vm_,
        'start_action': opts['start_action'],
        'parallel': opts['parallel'],
        'sock_dir': opts['sock_dir'],
        'conf_file': opts['conf_file'],
        'minion_pem': vm_['priv_key'],
        'minion_pub': vm_['pub_key'],
        'master_sign_pub_file': salt.config.get_cloud_config_value(
            'master_sign_pub_file', vm_, opts, default=None),
        'keep_tmp': opts['keep_tmp'],
        'sudo': salt.config.get_cloud_config_value(
            'sudo', vm_, opts, default=(ssh_username != 'root')
        ),
        'sudo_password': salt.config.get_cloud_config_value(
            'sudo_password', vm_, opts, default=None
        ),
        'tty': salt.config.get_cloud_config_value(
            'tty', vm_, opts, default=True
        ),
        'password': salt.config.get_cloud_config_value(
            'password', vm_, opts, search_global=False
        ),
        'key_filename': key_filename,
        'script_args': salt.config.get_cloud_config_value(
            'script_args', vm_, opts
        ),
        'script_env': salt.config.get_cloud_config_value(
            'script_env', vm_, opts
        ),
        'minion_conf': minion_conf,
        'force_minion_config': salt.config.get_cloud_config_value(
            'force_minion_config', vm_, opts, default=False
        ),
        'preseed_minion_keys': vm_.get('preseed_minion_keys', None),
        'display_ssh_output': salt.config.get_cloud_config_value(
            'display_ssh_output', vm_, opts, default=True
        ),
        'known_hosts_file': salt.config.get_cloud_config_value(
            'known_hosts_file', vm_, opts, default='/dev/null'
        ),
        'file_map': salt.config.get_cloud_config_value(
            'file_map', vm_, opts, default=None
        ),
        'maxtries': salt.config.get_cloud_config_value(
            'wait_for_passwd_maxtries', vm_, opts, default=15
        ),
        'preflight_cmds': salt.config.get_cloud_config_value(
            'preflight_cmds', vm_, opts, default=[]
        ),
        'cloud_grains': {'driver': vm_['driver'],
                         'provider': vm_['provider'],
                         'profile': vm_['profile']
                         }
    }

    inline_script_kwargs = deploy_kwargs.copy()  # make a copy at this point

    # forward any info about possible ssh gateway to deploy script
    # as some providers need also a 'gateway' configuration
    if 'gateway' in vm_:
        deploy_kwargs.update({'gateway': vm_['gateway']})

    # Deploy salt-master files, if necessary
    if salt.config.get_cloud_config_value('make_master', vm_, opts) is True:
        deploy_kwargs['make_master'] = True
        deploy_kwargs['master_pub'] = vm_['master_pub']
        deploy_kwargs['master_pem'] = vm_['master_pem']
        master_conf = master_config(opts, vm_)
        deploy_kwargs['master_conf'] = master_conf

        if master_conf.get('syndic_master', None):
            deploy_kwargs['make_syndic'] = True

    deploy_kwargs['make_minion'] = salt.config.get_cloud_config_value(
        'make_minion', vm_, opts, default=True
    )

    if saltify_driver:
        deploy_kwargs['wait_for_passwd_maxtries'] = 0  # No need to wait/retry with Saltify

    win_installer = salt.config.get_cloud_config_value(
        'win_installer', vm_, opts
    )
    if win_installer:
        deploy_kwargs['port'] = salt.config.get_cloud_config_value(
            'smb_port', vm_, opts, default=445
        )
        deploy_kwargs['win_installer'] = win_installer
        minion = minion_config(opts, vm_)
        deploy_kwargs['master'] = minion['master']
        deploy_kwargs['username'] = salt.config.get_cloud_config_value(
            'win_username', vm_, opts, default='Administrator'
        )
        win_pass = salt.config.get_cloud_config_value(
            'win_password', vm_, opts, default=''
        )
        if win_pass:
            deploy_kwargs['password'] = win_pass
        deploy_kwargs['use_winrm'] = salt.config.get_cloud_config_value(
            'use_winrm', vm_, opts, default=False
        )
        deploy_kwargs['winrm_port'] = salt.config.get_cloud_config_value(
            'winrm_port', vm_, opts, default=5986
        )
        deploy_kwargs['winrm_use_ssl'] = salt.config.get_cloud_config_value(
            'winrm_use_ssl', vm_, opts, default=True
        )
        deploy_kwargs['winrm_verify_ssl'] = salt.config.get_cloud_config_value(
            'winrm_verify_ssl', vm_, opts, default=True
        )
        if saltify_driver:
            deploy_kwargs['port_timeout'] = 1  # No need to wait/retry with Saltify

    # Store what was used to the deploy the VM
    event_kwargs = copy.deepcopy(deploy_kwargs)
    del event_kwargs['opts']
    del event_kwargs['minion_pem']
    del event_kwargs['minion_pub']
    del event_kwargs['sudo_password']
    if 'password' in event_kwargs:
        del event_kwargs['password']
    ret['deploy_kwargs'] = event_kwargs

    fire_event(
        'event',
        'executing deploy script',
        'salt/cloud/{0}/deploying'.format(vm_['name']),
        args={'kwargs': salt.utils.data.simple_types_filter(event_kwargs)},
        sock_dir=opts.get(
            'sock_dir',
            os.path.join(__opts__['sock_dir'], 'master')),
        transport=opts.get('transport', 'zeromq')
    )

    if inline_script_config and deploy_config is False:
        inline_script_deployed = run_inline_script(**inline_script_kwargs)
        if inline_script_deployed is not False:
            log.info('Inline script(s) ha(s|ve) run on %s', vm_['name'])
        ret['deployed'] = False
        return ret
    else:
        if win_installer:
            deployed = deploy_windows(**deploy_kwargs)
        else:
            deployed = deploy_script(**deploy_kwargs)

        if inline_script_config:
            inline_script_deployed = run_inline_script(**inline_script_kwargs)
            if inline_script_deployed is not False:
                log.info('Inline script(s) ha(s|ve) run on %s', vm_['name'])

        if deployed is not False:
            ret['deployed'] = True
            if deployed is not True:
                ret.update(deployed)
            log.info('Salt installed on %s', vm_['name'])
            return ret

    log.error('Failed to start Salt on host %s', vm_['name'])
    return {
        'Error': {
            'Not Deployed': 'Failed to start Salt on host {0}'.format(
                vm_['name']
            )
        }
    }