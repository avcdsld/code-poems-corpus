def run(image_id, name=None, tags=None, key_name=None, security_groups=None,
        user_data=None, instance_type='m1.small', placement=None,
        kernel_id=None, ramdisk_id=None, monitoring_enabled=None, vpc_id=None,
        vpc_name=None, subnet_id=None, subnet_name=None, private_ip_address=None,
        block_device_map=None, disable_api_termination=None,
        instance_initiated_shutdown_behavior=None, placement_group=None,
        client_token=None, security_group_ids=None, security_group_names=None,
        additional_info=None, tenancy=None, instance_profile_arn=None,
        instance_profile_name=None, ebs_optimized=None,
        network_interface_id=None, network_interface_name=None,
        region=None, key=None, keyid=None, profile=None, network_interfaces=None):
    #TODO: support multi-instance reservations
    '''
    Create and start an EC2 instance.

    Returns True if the instance was created; otherwise False.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_ec2.run ami-b80c2b87 name=myinstance

    image_id
        (string) – The ID of the image to run.
    name
        (string) - The name of the instance.
    tags
        (dict of key: value pairs) - tags to apply to the instance.
    key_name
        (string) – The name of the key pair with which to launch instances.
    security_groups
        (list of strings) – The names of the EC2 classic security groups with
        which to associate instances
    user_data
        (string) – The Base64-encoded MIME user data to be made available to the
        instance(s) in this reservation.
    instance_type
        (string) – The type of instance to run.  Note that some image types
        (e.g. hvm) only run on some instance types.
    placement
        (string) – The Availability Zone to launch the instance into.
    kernel_id
        (string) – The ID of the kernel with which to launch the instances.
    ramdisk_id
        (string) – The ID of the RAM disk with which to launch the instances.
    monitoring_enabled
        (bool) – Enable detailed CloudWatch monitoring on the instance.
    vpc_id
        (string) - ID of a VPC to bind the instance to.  Exclusive with vpc_name.
    vpc_name
        (string) - Name of a VPC to bind the instance to.  Exclusive with vpc_id.
    subnet_id
        (string) – The subnet ID within which to launch the instances for VPC.
    subnet_name
        (string) – The name of a subnet within which to launch the instances for VPC.
    private_ip_address
        (string) – If you’re using VPC, you can optionally use this parameter to
        assign the instance a specific available IP address from the subnet
        (e.g. 10.0.0.25).
    block_device_map
        (boto.ec2.blockdevicemapping.BlockDeviceMapping) – A BlockDeviceMapping
        data structure describing the EBS volumes associated with the Image.
        (string) - A string representation of a BlockDeviceMapping structure
        (dict) - A dict describing a BlockDeviceMapping structure

        YAML example:

        .. code-block:: yaml

            device-maps:
                /dev/sdb:
                    ephemeral_name: ephemeral0
                /dev/sdc:
                    ephemeral_name: ephemeral1
                /dev/sdd:
                    ephemeral_name: ephemeral2
                /dev/sde:
                    ephemeral_name: ephemeral3
                /dev/sdf:
                    size: 20
                    volume_type: gp2

    disable_api_termination
        (bool) – If True, the instances will be locked and will not be able to
        be terminated via the API.
    instance_initiated_shutdown_behavior
        (string) – Specifies whether the instance stops or terminates on
        instance-initiated shutdown. Valid values are: stop, terminate
    placement_group
        (string) – If specified, this is the name of the placement group in
        which the instance(s) will be launched.
    client_token
        (string) – Unique, case-sensitive identifier you provide to ensure
        idempotency of the request. Maximum 64 ASCII characters.
    security_group_ids
        (list of strings) – The ID(s) of the VPC security groups with which to
        associate instances.
    security_group_names
        (list of strings) – The name(s) of the VPC security groups with which to
        associate instances.
    additional_info
        (string) – Specifies additional information to make available to the
        instance(s).
    tenancy
        (string) – The tenancy of the instance you want to launch. An instance
        with a tenancy of ‘dedicated’ runs on single-tenant hardware and can
        only be launched into a VPC. Valid values are:”default” or “dedicated”.
        NOTE: To use dedicated tenancy you MUST specify a VPC subnet-ID as well.
    instance_profile_arn
        (string) – The Amazon resource name (ARN) of the IAM Instance Profile
        (IIP) to associate with the instances.
    instance_profile_name
        (string) – The name of the IAM Instance Profile (IIP) to associate with
        the instances.
    ebs_optimized
        (bool) – Whether the instance is optimized for EBS I/O. This
        optimization provides dedicated throughput to Amazon EBS and an
        optimized configuration stack to provide optimal EBS I/O performance.
        This optimization isn’t available with all instance types.
    network_interfaces
        (boto.ec2.networkinterface.NetworkInterfaceCollection) – A
        NetworkInterfaceCollection data structure containing the ENI
        specifications for the instance.
    network_interface_id
        (string) - ID of the network interface to attach to the instance
    network_interface_name
        (string) - Name of the network interface to attach to the instance

    '''
    if all((subnet_id, subnet_name)):
        raise SaltInvocationError('Only one of subnet_name or subnet_id may be '
                                  'provided.')
    if subnet_name:
        r = __salt__['boto_vpc.get_resource_id']('subnet', subnet_name,
                                                 region=region, key=key,
                                                 keyid=keyid, profile=profile)
        if 'id' not in r:
            log.warning('Couldn\'t resolve subnet name %s.', subnet_name)
            return False
        subnet_id = r['id']

    if all((security_group_ids, security_group_names)):
        raise SaltInvocationError('Only one of security_group_ids or '
                                  'security_group_names may be provided.')
    if security_group_names:
        security_group_ids = []
        for sgn in security_group_names:
            r = __salt__['boto_secgroup.get_group_id'](sgn, vpc_name=vpc_name,
                                                       region=region, key=key,
                                                       keyid=keyid, profile=profile)
            if not r:
                log.warning('Couldn\'t resolve security group name %s', sgn)
                return False
            security_group_ids += [r]

    network_interface_args = list(map(int, [network_interface_id is not None,
                                            network_interface_name is not None,
                                            network_interfaces is not None]))

    if sum(network_interface_args) > 1:
        raise SaltInvocationError('Only one of network_interface_id, '
                                  'network_interface_name or '
                                  'network_interfaces may be provided.')
    if network_interface_name:
        result = get_network_interface_id(network_interface_name,
                                          region=region, key=key,
                                          keyid=keyid,
                                          profile=profile)
        network_interface_id = result['result']
        if not network_interface_id:
            log.warning(
                "Given network_interface_name '%s' cannot be mapped to an "
                "network_interface_id", network_interface_name
            )

    if network_interface_id:
        interface = NetworkInterfaceSpecification(
            network_interface_id=network_interface_id,
            device_index=0)
    else:
        interface = NetworkInterfaceSpecification(
            subnet_id=subnet_id,
            groups=security_group_ids,
            device_index=0)

    if network_interfaces:
        interfaces_specs = [NetworkInterfaceSpecification(**x) for x in network_interfaces]
        interfaces = NetworkInterfaceCollection(*interfaces_specs)
    else:
        interfaces = NetworkInterfaceCollection(interface)

    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)

    reservation = conn.run_instances(image_id, key_name=key_name, security_groups=security_groups,
                                     user_data=user_data, instance_type=instance_type,
                                     placement=placement, kernel_id=kernel_id, ramdisk_id=ramdisk_id,
                                     monitoring_enabled=monitoring_enabled,
                                     private_ip_address=private_ip_address,
                                     block_device_map=_to_blockdev_map(block_device_map),
                                     disable_api_termination=disable_api_termination,
                                     instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior,
                                     placement_group=placement_group, client_token=client_token,
                                     additional_info=additional_info,
                                     tenancy=tenancy, instance_profile_arn=instance_profile_arn,
                                     instance_profile_name=instance_profile_name, ebs_optimized=ebs_optimized,
                                     network_interfaces=interfaces)
    if not reservation:
        log.warning('Instance could not be reserved')
        return False

    instance = reservation.instances[0]

    status = 'pending'
    while status == 'pending':
        time.sleep(5)
        status = instance.update()
    if status == 'running':
        if name:
            instance.add_tag('Name', name)
        if tags:
            instance.add_tags(tags)
        return {'instance_id': instance.id}
    else:
        log.warning(
            'Instance could not be started -- status is "%s"',
            status
        )