def present(name, auth=None, **kwargs):
    '''
    Ensure a subnet exists and is up-to-date

    name
        Name of the subnet

    network_name_or_id
        The unique name or ID of the attached network.
        If a non-unique name is supplied, an exception is raised.

    allocation_pools
        A list of dictionaries of the start and end addresses
        for the allocation pools

    gateway_ip
        The gateway IP address.

    dns_nameservers
        A list of DNS name servers for the subnet.

    host_routes
        A list of host route dictionaries for the subnet.

    ipv6_ra_mode
        IPv6 Router Advertisement mode.
        Valid values are: ‘dhcpv6-stateful’, ‘dhcpv6-stateless’, or ‘slaac’.

    ipv6_address_mode
        IPv6 address mode.
        Valid values are: ‘dhcpv6-stateful’, ‘dhcpv6-stateless’, or ‘slaac’.
    '''
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''}

    kwargs = __utils__['args.clean_kwargs'](**kwargs)

    __salt__['neutronng.setup_clouds'](auth)

    kwargs['subnet_name'] = name
    subnet = __salt__['neutronng.subnet_get'](name=name)

    if subnet is None:
        if __opts__['test']:
            ret['result'] = None
            ret['changes'] = kwargs
            ret['comment'] = 'Subnet will be created.'
            return ret

        new_subnet = __salt__['neutronng.subnet_create'](**kwargs)
        ret['changes'] = new_subnet
        ret['comment'] = 'Created subnet'
        return ret

    changes = __salt__['neutronng.compare_changes'](subnet, **kwargs)
    if changes:
        if __opts__['test'] is True:
            ret['result'] = None
            ret['changes'] = changes
            ret['comment'] = 'Project will be updated.'
            return ret

        # update_subnet does not support changing cidr,
        # so we have to delete and recreate the subnet in this case.
        if 'cidr' in changes or 'tenant_id' in changes:
            __salt__['neutronng.subnet_delete'](name=name)
            new_subnet = __salt__['neutronng.subnet_create'](**kwargs)
            ret['changes'] = new_subnet
            ret['comment'] = 'Deleted and recreated subnet'
            return ret

        __salt__['neutronng.subnet_update'](**kwargs)
        ret['changes'].update(changes)
        ret['comment'] = 'Updated subnet'

    return ret