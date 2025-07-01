def stop_server(jboss_config, host=None):
    '''
    Stop running jboss instance

    jboss_config
        Configuration dictionary with properties specified above.
    host
        The name of the host. JBoss domain mode only - and required if running in domain mode.
        The host name is the "name" attribute of the "host" element in host.xml

    CLI Example:

    .. code-block:: bash

        salt '*' jboss7.stop_server '{"cli_path": "integration.modules.sysmod.SysModuleTest.test_valid_docs", "controller": "10.11.12.13:9999", "cli_user": "jbossadm", "cli_password": "jbossadm"}'

       '''
    log.debug("======================== MODULE FUNCTION: jboss7.stop_server")
    if host is None:
        operation = ':shutdown'
    else:
        operation = '/host="{host}"/:shutdown'.format(host=host)
    shutdown_result = __salt__['jboss7_cli.run_operation'](jboss_config, operation, fail_on_error=False)
    # JBoss seems to occasionaly close the channel immediately when :shutdown is sent
    if shutdown_result['success'] or (not shutdown_result['success'] and 'Operation failed: Channel closed' in shutdown_result['stdout']):
        return shutdown_result
    else:
        raise Exception('''Cannot handle error, return code={retcode}, stdout='{stdout}', stderr='{stderr}' '''.format(**shutdown_result))