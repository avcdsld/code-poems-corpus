def enable(name, start=False, **kwargs):
    '''
    Start service ``name`` at boot.
    Returns ``True`` if operation is successful

    name
        the service's name

    start : False
        If ``True``, start the service once enabled.

    CLI Example:

    .. code-block:: bash

        salt '*' service.enable <name> [start=True]
    '''

    # non-existent service
    if not available(name):
        return False

    # if service is aliased, refuse to enable it
    alias = get_svc_alias()
    if name in alias:
        log.error('This service is aliased, enable its alias instead')
        return False

    # down_file: file that disables sv autostart
    svc_realpath = _get_svc_path(name)[0]
    down_file = os.path.join(svc_realpath, 'down')

    # if service already enabled, remove down_file to
    # let service starts on boot (as requested)
    if enabled(name):
        if os.path.exists(down_file):
            try:
                os.unlink(down_file)
            except OSError:
                log.error('Unable to remove file %s', down_file)
                return False
        return True

    # let's enable the service

    if not start:
        # create a temp 'down' file BEFORE enabling service.
        # will prevent sv from starting this service automatically.
        log.trace('need a temporary file %s', down_file)
        if not os.path.exists(down_file):
            try:
                salt.utils.files.fopen(down_file, "w").close()  # pylint: disable=resource-leakage
            except IOError:
                log.error('Unable to create file %s', down_file)
                return False

    # enable the service
    try:
        os.symlink(svc_realpath, _service_path(name))

    except IOError:
        # (attempt to) remove temp down_file anyway
        log.error('Unable to create symlink %s', down_file)
        if not start:
            os.unlink(down_file)
        return False

    # ensure sv is aware of this new service before continuing.
    # if not, down_file might be removed too quickly,
    # before 'sv' have time to take care about it.
    # Documentation indicates that a change is handled within 5 seconds.
    cmd = 'sv status {0}'.format(_service_path(name))
    retcode_sv = 1
    count_sv = 0
    while retcode_sv != 0 and count_sv < 10:
        time.sleep(0.5)
        count_sv += 1
        call = __salt__['cmd.run_all'](cmd)
        retcode_sv = call['retcode']

    # remove the temp down_file in any case.
    if (not start) and os.path.exists(down_file):
        try:
            os.unlink(down_file)
        except OSError:
            log.error('Unable to remove temp file %s', down_file)
            retcode_sv = 1

    # if an error happened, revert our changes
    if retcode_sv != 0:
        os.unlink(os.path.join([_service_path(name), name]))
        return False
    return True