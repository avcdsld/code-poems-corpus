def delete_interface(device_name, interface_name):
    '''
    .. versionadded:: 2019.2.0

    Delete an interface from a device.

    device_name
        The name of the device, e.g., ``edge_router``.

    interface_name
        The name of the interface, e.g., ``ae13``

    CLI Example:

    .. code-block:: bash

        salt myminion netbox.delete_interface edge_router ae13
    '''
    nb_device = get_('dcim', 'devices', name=device_name)
    nb_interface = _get('dcim', 'interfaces', auth_required=True, device_id=nb_device['id'], name=interface_name)
    if nb_interface:
        nb_interface.delete()
        return {'DELETE': {'dcim': {'interfaces': {nb_interface.id: nb_interface.name}}}}
    return False