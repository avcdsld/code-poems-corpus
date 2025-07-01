def ntp_configured(name,
                   service_running,
                   ntp_servers=None,
                   service_policy=None,
                   service_restart=False,
                   update_datetime=False):
    '''
    Ensures a host's NTP server configuration such as setting NTP servers, ensuring the
    NTP daemon is running or stopped, or restarting the NTP daemon for the ESXi host.

    name
        Name of the state.

    service_running
        Ensures the running state of the ntp daemon for the host. Boolean value where
        ``True`` indicates that ntpd should be running and ``False`` indicates that it
        should be stopped.

    ntp_servers
        A list of servers that should be added to the ESXi host's NTP configuration.

    service_policy
        The policy to set for the NTP service.

        .. note::

            When setting the service policy to ``off`` or ``on``, you *must* quote the
            setting. If you don't, the yaml parser will set the string to a boolean,
            which will cause trouble checking for stateful changes and will error when
            trying to set the policy on the ESXi host.


    service_restart
        If set to ``True``, the ntp daemon will be restarted, regardless of its previous
        running state. Default is ``False``.

    update_datetime
        If set to ``True``, the date/time on the given host will be updated to UTC.
        Default setting is ``False``. This option should be used with caution since
        network delays and execution delays can result in time skews.

    Example:

    .. code-block:: yaml

        configure-host-ntp:
          esxi.ntp_configured:
            - service_running: True
            - ntp_servers:
              - 192.174.1.100
              - 192.174.1.200
            - service_policy: 'on'
            - service_restart: True

    '''
    ret = {'name': name,
           'result': False,
           'changes': {},
           'comment': ''}
    esxi_cmd = 'esxi.cmd'
    host = __pillar__['proxy']['host']
    ntpd = 'ntpd'

    ntp_config = __salt__[esxi_cmd]('get_ntp_config').get(host)
    ntp_running = __salt__[esxi_cmd]('get_service_running',
                                     service_name=ntpd).get(host)
    error = ntp_running.get('Error')
    if error:
        ret['comment'] = 'Error: {0}'.format(error)
        return ret
    ntp_running = ntp_running.get(ntpd)

    # Configure NTP Servers for the Host
    if ntp_servers and set(ntp_servers) != set(ntp_config):
        # Only run the command if not using test=True
        if not __opts__['test']:
            response = __salt__[esxi_cmd]('set_ntp_config',
                                          ntp_servers=ntp_servers).get(host)
            error = response.get('Error')
            if error:
                ret['comment'] = 'Error: {0}'.format(error)
                return ret
        # Set changes dictionary for ntp_servers
        ret['changes'].update({'ntp_servers':
                              {'old': ntp_config,
                               'new': ntp_servers}})

    # Configure service_running state
    if service_running != ntp_running:
        # Only run the command if not using test=True
        if not __opts__['test']:
            # Start ntdp if service_running=True
            if ntp_running is True:
                response = __salt__[esxi_cmd]('service_start',
                                              service_name=ntpd).get(host)
                error = response.get('Error')
                if error:
                    ret['comment'] = 'Error: {0}'.format(error)
                    return ret
            # Stop ntpd if service_running=False
            else:
                response = __salt__[esxi_cmd]('service_stop',
                                              service_name=ntpd).get(host)
                error = response.get('Error')
                if error:
                    ret['comment'] = 'Error: {0}'.format(error)
                    return ret
        ret['changes'].update({'service_running':
                              {'old': ntp_running,
                               'new': service_running}})

    # Configure service_policy
    if service_policy:
        current_service_policy = __salt__[esxi_cmd]('get_service_policy',
                                                    service_name=ntpd).get(host)
        error = current_service_policy.get('Error')
        if error:
            ret['comment'] = 'Error: {0}'.format(error)
            return ret
        current_service_policy = current_service_policy.get(ntpd)

        if service_policy != current_service_policy:
            # Only run the command if not using test=True
            if not __opts__['test']:
                response = __salt__[esxi_cmd]('set_service_policy',
                                              service_name=ntpd,
                                              service_policy=service_policy).get(host)
                error = response.get('Error')
                if error:
                    ret['comment'] = 'Error: {0}'.format(error)
                    return ret
            ret['changes'].update({'service_policy':
                                  {'old': current_service_policy,
                                   'new': service_policy}})

    # Update datetime, if requested.
    if update_datetime:
        # Only run the command if not using test=True
        if not __opts__['test']:
            response = __salt__[esxi_cmd]('update_host_datetime').get(host)
            error = response.get('Error')
            if error:
                ret['comment'] = 'Error: {0}'.format(error)
                return ret
        ret['changes'].update({'update_datetime':
                              {'old': '',
                               'new': 'Host datetime was updated.'}})

    # Restart ntp_service if service_restart=True
    if service_restart:
        # Only run the command if not using test=True
        if not __opts__['test']:
            response = __salt__[esxi_cmd]('service_restart',
                                          service_name=ntpd).get(host)
            error = response.get('Error')
            if error:
                ret['comment'] = 'Error: {0}'.format(error)
                return ret
        ret['changes'].update({'service_restart':
                              {'old': '',
                               'new': 'NTP Daemon Restarted.'}})

    ret['result'] = True
    if ret['changes'] == {}:
        ret['comment'] = 'NTP is already in the desired state.'
        return ret

    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'NTP state will change.'

    return ret