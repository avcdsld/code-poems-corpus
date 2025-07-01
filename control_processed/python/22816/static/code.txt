def list_cidr_ips_ipv6(cidr):
    '''
    Get a list of IPv6 addresses from a CIDR.

    CLI example::

        salt myminion netaddress.list_cidr_ips_ipv6 192.168.0.0/20
    '''
    ips = netaddr.IPNetwork(cidr)
    return [six.text_type(ip.ipv6()) for ip in list(ips)]