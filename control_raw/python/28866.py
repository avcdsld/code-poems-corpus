def cleanup(keep_latest=True):
    '''
    Remove all unused kernel packages from the system.

    keep_latest : True
        In the event that the active kernel is not the latest one installed, setting this to True
        will retain the latest kernel package, in addition to the active one. If False, all kernel
        packages other than the active one will be removed.

    CLI Example:

    .. code-block:: bash

        salt '*' kernelpkg.cleanup
    '''
    removed = []

    # Loop over all installed kernel packages
    for kernel in list_installed():

        # Keep the active kernel package
        if kernel == active():
            continue

        # Optionally keep the latest kernel package
        if keep_latest and kernel == latest_installed():
            continue

        # Remove the kernel package
        removed.extend(remove(kernel)['removed'])

    return {'removed': removed}