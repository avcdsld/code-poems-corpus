def ip_addrs6(interface=None, include_loopback=False, cidr=None):
    '''
    Returns a list of IPv6 addresses assigned to the host.

    interface
        Only IP addresses from that interface will be returned.

    include_loopback : False
        Include loopback ::1 IPv6 address.

    cidr
        Describes subnet using CIDR notation and only IPv6 addresses that belong
        to this subnet will be returned.

        .. versionchanged:: 2019.2.0

    CLI Example:

    .. code-block:: bash

        salt '*' network.ip_addrs6
        salt '*' network.ip_addrs6 cidr=2000::/3
    '''
    addrs = salt.utils.network.ip_addrs6(interface=interface,
                                        include_loopback=include_loopback)
    if cidr:
        return [i for i in addrs if salt.utils.network.in_subnet(cidr, [i])]
    else:
        return addrs