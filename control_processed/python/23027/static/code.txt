def network_running(name,
                    bridge,
                    forward,
                    vport=None,
                    tag=None,
                    autostart=True,
                    connection=None,
                    username=None,
                    password=None):
    '''
    Defines and starts a new network with specified arguments.

    :param connection: libvirt connection URI, overriding defaults

        .. versionadded:: 2019.2.0
    :param username: username to connect with, overriding defaults

        .. versionadded:: 2019.2.0
    :param password: password to connect with, overriding defaults

        .. versionadded:: 2019.2.0

    .. code-block:: yaml

        domain_name:
          virt.network_define

    .. code-block:: yaml

        network_name:
          virt.network_define:
            - bridge: main
            - forward: bridge
            - vport: openvswitch
            - tag: 180
            - autostart: True

    '''
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''
           }

    try:
        info = __salt__['virt.network_info'](name, connection=connection, username=username, password=password)
        if info:
            if info['active']:
                ret['comment'] = 'Network {0} exists and is running'.format(name)
            else:
                __salt__['virt.network_start'](name, connection=connection, username=username, password=password)
                ret['changes'][name] = 'Network started'
                ret['comment'] = 'Network {0} started'.format(name)
        else:
            __salt__['virt.network_define'](name,
                                            bridge,
                                            forward,
                                            vport,
                                            tag=tag,
                                            autostart=autostart,
                                            start=True,
                                            connection=connection,
                                            username=username,
                                            password=password)
            ret['changes'][name] = 'Network defined and started'
            ret['comment'] = 'Network {0} defined and started'.format(name)
    except libvirt.libvirtError as err:
        ret['result'] = False
        ret['comment'] = err.get_error_message()

    return ret