def is_ipv4_filter(ip, options=None):
    '''
    Returns a bool telling if the value passed to it was a valid IPv4 address.

    ip
        The IP address.

    net: False
        Consider IP addresses followed by netmask.

    options
        CSV of options regarding the nature of the IP address. E.g.: loopback, multicast, private etc.
    '''
    _is_ipv4 = _is_ipv(ip, 4, options=options)
    return isinstance(_is_ipv4, six.string_types)