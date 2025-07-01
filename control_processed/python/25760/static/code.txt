def create(name,
           level,
           devices,
           metadata='default',
           test_mode=False,
           **kwargs):
    '''
    Create a RAID device.

    .. versionchanged:: 2014.7.0

    .. warning::
        Use with CAUTION, as this function can be very destructive if not used
        properly!

    CLI Examples:

    .. code-block:: bash

        salt '*' raid.create /dev/md0 level=1 chunk=256 devices="['/dev/xvdd', '/dev/xvde']" test_mode=True

    .. note::

        Adding ``test_mode=True`` as an argument will print out the mdadm
        command that would have been run.

    name
        The name of the array to create.

    level
        The RAID level to use when creating the raid.

    devices
        A list of devices used to build the array.

    metadata
        Version of metadata to use when creating the array.

    kwargs
        Optional arguments to be passed to mdadm.

    returns
        test_mode=True:
            Prints out the full command.
        test_mode=False (Default):
            Executes command on remote the host(s) and
            Prints out the mdadm output.

    .. note::

        It takes time to create a RAID array. You can check the progress in
        "resync_status:" field of the results from the following command:

        .. code-block:: bash

            salt '*' raid.detail /dev/md0

    For more info, read the ``mdadm(8)`` manpage
    '''
    opts = []
    raid_devices = len(devices)

    for key in kwargs:
        if not key.startswith('__'):
            opts.append('--{0}'.format(key))
            if kwargs[key] is not True:
                opts.append(six.text_type(kwargs[key]))
        if key == 'spare-devices':
            raid_devices -= int(kwargs[key])

    cmd = ['mdadm',
           '-C', name,
           '-R',
           '-v',
           '-l', six.text_type(level),
           ] + opts + [
           '-e', six.text_type(metadata),
           '-n', six.text_type(raid_devices),
           ] + devices

    cmd_str = ' '.join(cmd)

    if test_mode is True:
        return cmd_str
    elif test_mode is False:
        return __salt__['cmd.run'](cmd, python_shell=False)