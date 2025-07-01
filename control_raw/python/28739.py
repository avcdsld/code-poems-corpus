def online(zpool, *vdevs, **kwargs):
    '''
    .. versionadded:: 2015.5.0

    Ensure that the specified devices are online

    zpool : string
        name of storage pool

    vdevs : string
        one or more devices

    expand : boolean
        Expand the device to use all available space.

        .. note::

            If the device is part of a mirror or raidz then all devices must be
            expanded before the new space will become available to the pool.

    CLI Example:

    .. code-block:: bash

        salt '*' zpool.online myzpool /path/to/vdev1 [...]

    '''
    ## Configure pool
    # default options
    flags = []
    target = []

    # set flags and options
    if kwargs.get('expand', False):
        flags.append('-e')
    target.append(zpool)
    if vdevs:
        target.extend(vdevs)

    ## Configure pool
    # NOTE: initialize the defaults
    flags = []
    target = []

    # NOTE: set extra config based on kwargs
    if kwargs.get('expand', False):
        flags.append('-e')

    # NOTE: append the pool name and specifications
    target.append(zpool)
    target.extend(vdevs)

    ## Bring online device
    res = __salt__['cmd.run_all'](
        __utils__['zfs.zpool_command'](
            command='online',
            flags=flags,
            target=target,
        ),
        python_shell=False,
    )

    return __utils__['zfs.parse_command_result'](res, 'onlined')