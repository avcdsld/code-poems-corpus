def associate_network_acl_to_subnet(network_acl_id=None, subnet_id=None,
                                    network_acl_name=None,
                                    subnet_name=None, region=None,
                                    key=None, keyid=None, profile=None):
    '''
    Given a network acl and subnet ids or names, associate a network acl to a subnet.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_vpc.associate_network_acl_to_subnet \\
                network_acl_id='acl-5fb85d36' subnet_id='subnet-6a1fe403'

    .. code-block:: bash

        salt myminion boto_vpc.associate_network_acl_to_subnet \\
                network_acl_id='myacl' subnet_id='mysubnet'

    '''

    if network_acl_name:
        network_acl_id = _get_resource_id('network_acl', network_acl_name,
                                          region=region, key=key,
                                          keyid=keyid, profile=profile)
        if not network_acl_id:
            return {'associated': False,
                    'error': {'message': 'Network ACL {0} does not exist.'.format(network_acl_name)}}
    if subnet_name:
        subnet_id = _get_resource_id('subnet', subnet_name,
                                     region=region, key=key,
                                     keyid=keyid, profile=profile)
        if not subnet_id:
            return {'associated': False,
                    'error': {'message': 'Subnet {0} does not exist.'.format(subnet_name)}}
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        association_id = conn.associate_network_acl(network_acl_id, subnet_id)
        if association_id:
            log.info('Network ACL with id %s was associated with subnet %s',
                     network_acl_id, subnet_id)

            return {'associated': True, 'id': association_id}
        else:
            log.warning('Network ACL with id %s was not associated with subnet %s',
                        network_acl_id, subnet_id)
            return {'associated': False, 'error': {'message': 'ACL could not be assocaited.'}}
    except BotoServerError as e:
        return {'associated': False, 'error': __utils__['boto.get_error'](e)}