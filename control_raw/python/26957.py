def snapshot_id_to_name(name, snap_id, strict=False, runas=None):
    '''
    Attempt to convert a snapshot ID to a snapshot name.  If the snapshot has
    no name or if the ID is not found or invalid, an empty string will be returned

    :param str name:
        Name/ID of VM whose snapshots are inspected

    :param str snap_id:
        ID of the snapshot

    :param bool strict:
        Raise an exception if a name cannot be found for the given ``snap_id``

    :param str runas:
        The user that the prlctl command will be run as

    Example data

    .. code-block:: yaml

        ID: {a5b8999f-5d95-4aff-82de-e515b0101b66}
        Name: original
        Date: 2016-03-04 10:50:34
        Current: yes
        State: poweroff
        Description: original state

    CLI Example:

    .. code-block:: bash

        salt '*' parallels.snapshot_id_to_name macvm a5b8999f-5d95-4aff-82de-e515b0101b66 runas=macdev
    '''
    # Validate VM name and snapshot ID
    name = salt.utils.data.decode(name)
    if not re.match(GUID_REGEX, snap_id):
        raise SaltInvocationError(
            'Snapshot ID "{0}" is not a GUID'.format(salt.utils.data.decode(snap_id))
        )

    # Get the snapshot information of the snapshot having the requested ID
    info = prlctl('snapshot-list', [name, '--id', snap_id], runas=runas)

    # Parallels desktop returned no information for snap_id
    if not info:
        raise SaltInvocationError(
            'No snapshots for VM "{0}" have ID "{1}"'.format(name, snap_id)
        )

    # Try to interpret the information
    try:
        data = salt.utils.yaml.safe_load(info)
    except salt.utils.yaml.YAMLError as err:
        log.warning(
            'Could not interpret snapshot data returned from prlctl: %s', err
        )
        data = {}

    # Find the snapshot name
    if isinstance(data, dict):
        snap_name = data.get('Name', '')
        # If snapshot name is of type NoneType, then the snapshot is unnamed
        if snap_name is None:
            snap_name = ''
    else:
        log.warning(
            'Could not interpret snapshot data returned from prlctl: '
            'data is not formed as a dictionary: %s', data
        )
        snap_name = ''

    # Raise or return the result
    if not snap_name and strict:
        raise SaltInvocationError(
            'Could not find a snapshot name for snapshot ID "{0}" of VM '
            '"{1}"'.format(snap_id, name)
        )
    return salt.utils.data.decode(snap_name)