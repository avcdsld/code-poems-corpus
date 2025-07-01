def list_datastores(kwargs=None, call=None):
    '''
    List all the datastores for this VMware environment

    CLI Example:

    .. code-block:: bash

        salt-cloud -f list_datastores my-vmware-config
    '''
    if call != 'function':
        raise SaltCloudSystemExit(
            'The list_datastores function must be called with '
            '-f or --function.'
        )

    return {'Datastores': salt.utils.vmware.list_datastores(_get_si())}