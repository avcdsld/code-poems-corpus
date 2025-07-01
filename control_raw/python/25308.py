def rename_datastore(datastore_name, new_datastore_name,
                     service_instance=None):
    '''
    Renames a datastore. The datastore needs to be visible to the proxy.

    datastore_name
        Current datastore name.

    new_datastore_name
        New datastore name.

    service_instance
        Service instance (vim.ServiceInstance) of the vCenter/ESXi host.
        Default is None.

    .. code-block:: bash

        salt '*' vsphere.rename_datastore old_name new_name
    '''
    # Argument validation
    log.trace('Renaming datastore %s to %s', datastore_name, new_datastore_name)
    target = _get_proxy_target(service_instance)
    datastores = salt.utils.vmware.get_datastores(
        service_instance,
        target,
        datastore_names=[datastore_name])
    if not datastores:
        raise VMwareObjectRetrievalError('Datastore \'{0}\' was not found'
                                         ''.format(datastore_name))
    ds = datastores[0]
    salt.utils.vmware.rename_datastore(ds, new_datastore_name)
    return True