def list_volume_snapshots(volume_id, profile, **libcloud_kwargs):
    '''
    Return a list of storage volumes snapshots for this cloud

    :param volume_id: The volume identifier
    :type  volume_id: ``str``

    :param profile: The profile key
    :type  profile: ``str``

    :param libcloud_kwargs: Extra arguments for the driver's list_volume_snapshots method
    :type  libcloud_kwargs: ``dict``

    CLI Example:

    .. code-block:: bash

        salt myminion libcloud_compute.list_volume_snapshots vol1 profile1
    '''
    conn = _get_driver(profile=profile)
    libcloud_kwargs = salt.utils.args.clean_kwargs(**libcloud_kwargs)
    volume = _get_by_id(conn.list_volumes(), volume_id)
    snapshots = conn.list_volume_snapshots(volume, **libcloud_kwargs)

    ret = []
    for snapshot in snapshots:
        ret.append(_simple_volume_snapshot(snapshot))
    return ret