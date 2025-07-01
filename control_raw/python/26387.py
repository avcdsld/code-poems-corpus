def create_interface(device_name,
                     interface_name,
                     mac_address=None,
                     description=None,
                     enabled=None,
                     lag=None,
                     lag_parent=None,
                     form_factor=None):
    '''
    .. versionadded:: 2019.2.0

    Attach an interface to a device. If not all arguments are provided,
    they will default to Netbox defaults.

    device_name
        The name of the device, e.g., ``edge_router``
    interface_name
        The name of the interface, e.g., ``TenGigE0/0/0/0``
    mac_address
        String of mac address, e.g., ``50:87:89:73:92:C8``
    description
        String of interface description, e.g., ``NTT``
    enabled
        String of boolean interface status, e.g., ``True``
    lag:
        Boolean of interface lag status, e.g., ``True``
    lag_parent
        String of interface lag parent name, e.g., ``ae13``
    form_factor
        Integer of form factor id, obtained through _choices API endpoint, e.g., ``200``

    CLI Example:

    .. code-block:: bash

        salt myminion netbox.create_interface edge_router ae13 description="Core uplink"
    '''
    nb_device = get_('dcim', 'devices', name=device_name)
    if not nb_device:
        return False
    if lag_parent:
        lag_interface = get_('dcim', 'interfaces', device_id=nb_device['id'], name=lag_parent)
        if not lag_interface:
            return False
    if not description:
        description = ''
    if not enabled:
        enabled = 'false'
    # Set default form factor to 1200. This maps to SFP+ (10GE). This should be addressed by
    # the _choices endpoint.
    payload = {'device': nb_device['id'], 'name': interface_name,
               'description': description, 'enabled': enabled, 'form_factor': 1200}
    if form_factor is not None:
        payload['form_factor'] = form_factor
    if lag:
        payload['form_factor'] = 200
    if lag_parent:
        payload['lag'] = lag_interface['id']
    if mac_address:
        payload['mac_address'] = mac_address
    nb_interface = get_('dcim', 'interfaces', device_id=nb_device['id'], name=interface_name)
    if not nb_interface:
        nb_interface = _add('dcim', 'interfaces', payload)
    if nb_interface:
        return {'dcim': {'interfaces': {nb_interface['id']: payload}}}
    else:
        return nb_interface