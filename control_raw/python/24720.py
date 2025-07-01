def start(name, call=None):
    '''
    Start a VM.

    .. versionadded:: 2016.3.0

    name
        The name of the VM to start.

    CLI Example:

    .. code-block:: bash

        salt-cloud -a start my-vm
    '''
    if call != 'action':
        raise SaltCloudSystemExit(
            'The start action must be called with -a or --action.'
        )

    log.info('Starting node %s', name)

    return vm_action(name, kwargs={'action': 'resume'}, call=call)