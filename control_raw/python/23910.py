def in_subnet(cidr, addr=None):
    '''
    Returns True if host or (any of) addrs is within specified subnet, otherwise False
    '''
    try:
        cidr = ipaddress.ip_network(cidr)
    except ValueError:
        log.error('Invalid CIDR \'%s\'', cidr)
        return False

    if addr is None:
        addr = ip_addrs()
        addr.extend(ip_addrs6())
    elif not isinstance(addr, (list, tuple)):
        addr = (addr,)

    return any(ipaddress.ip_address(item) in cidr for item in addr)