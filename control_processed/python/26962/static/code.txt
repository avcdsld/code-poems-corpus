def delete_snapshot(name, snap_name, runas=None, all=False):
    '''
    Delete a snapshot

    .. note::

        Deleting a snapshot from which other snapshots are dervied will not
        delete the derived snapshots

    :param str name:
        Name/ID of VM whose snapshot will be deleted

    :param str snap_name:
        Name/ID of snapshot to delete

    :param str runas:
        The user that the prlctl command will be run as

    :param bool all:
        Delete all snapshots having the name given

        .. versionadded:: 2016.11.0

    Example:

    .. code-block:: bash

        salt '*' parallels.delete_snapshot macvm 'unneeded snapshot' runas=macdev
        salt '*' parallels.delete_snapshot macvm 'Snapshot for linked clone' all=True runas=macdev
    '''
    # strict means raise an error if multiple snapshot IDs found for the name given
    strict = not all

    # Validate VM and snapshot names
    name = salt.utils.data.decode(name)
    snap_ids = _validate_snap_name(name, snap_name, strict=strict, runas=runas)
    if isinstance(snap_ids, six.string_types):
        snap_ids = [snap_ids]

    # Delete snapshot(s)
    ret = {}
    for snap_id in snap_ids:
        snap_id = snap_id.strip('{}')
        # Construct argument list
        args = [name, '--id', snap_id]

        # Execute command
        ret[snap_id] = prlctl('snapshot-delete', args, runas=runas)

    # Return results
    ret_keys = list(ret.keys())
    if len(ret_keys) == 1:
        return ret[ret_keys[0]]
    else:
        return ret