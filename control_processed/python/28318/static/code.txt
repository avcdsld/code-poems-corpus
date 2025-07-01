def _to_blockdev_map(thing):
    '''
    Convert a string, or a json payload, or a dict in the right
    format, into a boto.ec2.blockdevicemapping.BlockDeviceMapping as
    needed by instance_present().  The following YAML is a direct
    representation of what is expected by the underlying boto EC2 code.

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

    '''
    if not thing:
        return None
    if isinstance(thing, BlockDeviceMapping):
        return thing
    if isinstance(thing, six.string_types):
        thing = salt.utils.json.loads(thing)
    if not isinstance(thing, dict):
        log.error("Can't convert '%s' of type %s to a "
                  "boto.ec2.blockdevicemapping.BlockDeviceMapping", thing, type(thing))
        return None

    bdm = BlockDeviceMapping()
    for d, t in six.iteritems(thing):
        bdt = BlockDeviceType(ephemeral_name=t.get('ephemeral_name'),
                              no_device=t.get('no_device', False),
                              volume_id=t.get('volume_id'),
                              snapshot_id=t.get('snapshot_id'),
                              status=t.get('status'),
                              attach_time=t.get('attach_time'),
                              delete_on_termination=t.get('delete_on_termination', False),
                              size=t.get('size'),
                              volume_type=t.get('volume_type'),
                              iops=t.get('iops'),
                              encrypted=t.get('encrypted'))
        bdm[d] = bdt

    return bdm