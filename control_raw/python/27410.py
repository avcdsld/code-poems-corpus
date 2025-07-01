def add_dns(ip, interface='Local Area Connection', index=1):
    '''
    Add the DNS server to the network interface
    (index starts from 1)

    Note: if the interface DNS is configured by DHCP, all the DNS servers will
    be removed from the interface and the requested DNS will be the only one

    CLI Example:

    .. code-block:: bash

        salt '*' win_dns_client.add_dns <ip> <interface> <index>
    '''
    servers = get_dns_servers(interface)

    # Return False if could not find the interface
    if servers is False:
        return False

    # Return true if configured
    try:
        if servers[index - 1] == ip:
            return True
    except IndexError:
        pass

    # If configured in the wrong order delete it
    if ip in servers:
        rm_dns(ip, interface)

    cmd = ['netsh', 'interface', 'ip', 'add', 'dns',
           interface, ip, 'index={0}'.format(index), 'validate=no']

    return __salt__['cmd.retcode'](cmd, python_shell=False) == 0