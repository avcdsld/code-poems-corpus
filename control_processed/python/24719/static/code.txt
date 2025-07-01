def reboot(name, call=None):
    '''
    Reboot a VM.

    .. versionadded:: 2016.3.0

    name
        The name of the VM to reboot.

    CLI Example:

    .. code-block:: bash

        salt-cloud -a reboot my-vm
    '''
    if call != 'action':
        raise SaltCloudSystemExit(
            'The start action must be called with -a or --action.'
        )

    log.info('Rebooting node %s', name)

    return vm_action(name, kwargs={'action': 'reboot'}, call=call)