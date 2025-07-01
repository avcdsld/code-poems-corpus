def create_dhcp_options(domain_name=None, domain_name_servers=None, ntp_servers=None,
                        netbios_name_servers=None, netbios_node_type=None,
                        dhcp_options_name=None, tags=None, vpc_id=None, vpc_name=None,
                        region=None, key=None, keyid=None, profile=None):
    '''
    Given valid DHCP options, create a DHCP options record, optionally associating it with
    an existing VPC.

    Returns True if the DHCP options record was created and returns False if the DHCP options record was not deleted.

    .. versionchanged:: 2015.8.0
        Added vpc_name and vpc_id arguments

    CLI Example:

    .. code-block:: bash

        salt myminion boto_vpc.create_dhcp_options domain_name='example.com' \\
                domain_name_servers='[1.2.3.4]' ntp_servers='[5.6.7.8]' \\
                netbios_name_servers='[10.0.0.1]' netbios_node_type=1 \\
                vpc_name='myvpc'

    '''

    try:
        if vpc_id or vpc_name:
            vpc_id = check_vpc(vpc_id, vpc_name, region, key, keyid, profile)
            if not vpc_id:
                return {'created': False,
                        'error': {'message': 'VPC {0} does not exist.'.format(vpc_name or vpc_id)}}

        r = _create_resource('dhcp_options', name=dhcp_options_name, domain_name=domain_name,
                             domain_name_servers=domain_name_servers,
                             ntp_servers=ntp_servers, netbios_name_servers=netbios_name_servers,
                             netbios_node_type=netbios_node_type,
                             region=region, key=key, keyid=keyid,
                             profile=profile)
        if r.get('created') and vpc_id:
            conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
            conn.associate_dhcp_options(r['id'], vpc_id)
            log.info(
                'Associated options %s to VPC %s',
                r['id'], vpc_name or vpc_id
            )
        return r
    except BotoServerError as e:
        return {'created': False, 'error': __utils__['boto.get_error'](e)}