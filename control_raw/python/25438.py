def attach_disk(name=None, kwargs=None, call=None):
    '''
    Attach an existing disk to an existing instance.

    CLI Example:

    .. code-block:: bash

        salt-cloud -a attach_disk myinstance disk_name=mydisk mode=READ_WRITE
    '''
    if call != 'action':
        raise SaltCloudSystemExit(
            'The attach_disk action must be called with -a or --action.'
        )

    if not name:
        log.error(
            'Must specify an instance name.'
        )
        return False
    if not kwargs or 'disk_name' not in kwargs:
        log.error(
            'Must specify a disk_name to attach.'
        )
        return False

    node_name = name
    disk_name = kwargs['disk_name']
    mode = kwargs.get('mode', 'READ_WRITE').upper()
    boot = kwargs.get('boot', False)
    auto_delete = kwargs.get('auto_delete', False)
    if boot and boot.lower() in ['true', 'yes', 'enabled']:
        boot = True
    else:
        boot = False

    if mode not in ['READ_WRITE', 'READ_ONLY']:
        log.error(
            'Mode must be either READ_ONLY or (default) READ_WRITE.'
        )
        return False

    conn = get_conn()
    node = conn.ex_get_node(node_name)
    disk = conn.ex_get_volume(disk_name)

    __utils__['cloud.fire_event'](
        'event',
        'attach disk',
        'salt/cloud/disk/attaching',
        args={
            'name': node_name,
            'disk_name': disk_name,
            'mode': mode,
            'boot': boot,
        },
        sock_dir=__opts__['sock_dir'],
        transport=__opts__['transport']
    )

    result = conn.attach_volume(node, disk, ex_mode=mode, ex_boot=boot,
                                ex_auto_delete=auto_delete)

    __utils__['cloud.fire_event'](
        'event',
        'attached disk',
        'salt/cloud/disk/attached',
        args={
            'name': node_name,
            'disk_name': disk_name,
            'mode': mode,
            'boot': boot,
        },
        sock_dir=__opts__['sock_dir'],
        transport=__opts__['transport']
    )
    return result