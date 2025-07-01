def set_dhcp_only_all(interface):
    '''
    Configure specified adapter to use DHCP only

    Change adapter mode to TCP/IP. If previous adapter mode was EtherCAT, the target will need reboot.

    :param str interface: interface label
    :return: True if the settings were applied, otherwise an exception will be thrown.
    :rtype: bool

    CLI Example:

    .. code-block:: bash

        salt '*' ip.dhcp_only_all interface-label
    '''
    if not __grains__['lsb_distrib_id'] == 'nilrt':
        raise salt.exceptions.CommandExecutionError('Not supported in this version')
    initial_mode = _get_adapter_mode_info(interface)
    _save_config(interface, 'Mode', 'TCPIP')
    _save_config(interface, 'dhcpenabled', '1')
    _save_config(interface, 'linklocalenabled', '0')
    if initial_mode == 'ethercat':
        __salt__['system.set_reboot_required_witnessed']()
    else:
        _restart(interface)
    return True