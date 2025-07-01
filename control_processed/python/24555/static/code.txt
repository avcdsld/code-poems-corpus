def get_host_ipv6addr_info(ipv6addr=None, mac=None,
                                        discovered_data=None,
                                        return_fields=None, **api_opts):
    '''
    Get host ipv6addr information

    CLI Example:

    .. code-block:: bash

        salt-call infoblox.get_host_ipv6addr_info ipv6addr=2001:db8:85a3:8d3:1349:8a2e:370:7348
    '''
    infoblox = _get_infoblox(**api_opts)
    return infoblox.get_host_ipv6addr_object(ipv6addr, mac, discovered_data, return_fields)