def shutdown_host(kwargs=None, call=None):
    '''
    Shut down the specified host system in this VMware environment

    .. note::

        If the host system is not in maintenance mode, it will not be shut down. If you
        want to shut down the host system regardless of whether it is in maintenance mode,
        set ``force=True``. Default is ``force=False``.

    CLI Example:

    .. code-block:: bash

        salt-cloud -f shutdown_host my-vmware-config host="myHostSystemName" [force=True]
    '''
    if call != 'function':
        raise SaltCloudSystemExit(
            'The shutdown_host function must be called with '
            '-f or --function.'
        )

    host_name = kwargs.get('host') if kwargs and 'host' in kwargs else None
    force = _str_to_bool(kwargs.get('force')) if kwargs and 'force' in kwargs else False

    if not host_name:
        raise SaltCloudSystemExit(
            'You must specify name of the host system.'
        )

    # Get the service instance
    si = _get_si()

    host_ref = salt.utils.vmware.get_mor_by_property(si, vim.HostSystem, host_name)
    if not host_ref:
        raise SaltCloudSystemExit(
            'Specified host system does not exist.'
        )

    if host_ref.runtime.connectionState == 'notResponding':
        raise SaltCloudSystemExit(
            'Specified host system cannot be shut down in it\'s current state (not responding).'
        )

    if not host_ref.capability.rebootSupported:
        raise SaltCloudSystemExit(
            'Specified host system does not support shutdown.'
        )

    if not host_ref.runtime.inMaintenanceMode and not force:
        raise SaltCloudSystemExit(
            'Specified host system is not in maintenance mode. Specify force=True to '
            'force reboot even if there are virtual machines running or other operations '
            'in progress.'
        )

    try:
        host_ref.ShutdownHost_Task(force)
    except Exception as exc:
        log.error(
            'Error while shutting down host %s: %s',
            host_name, exc,
            # Show the traceback if the debug logging level is enabled
            exc_info_on_loglevel=logging.DEBUG
        )
        return {host_name: 'failed to shut down host'}

    return {host_name: 'shut down host'}