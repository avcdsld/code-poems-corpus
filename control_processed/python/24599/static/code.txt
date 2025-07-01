def get_interface(iface):
    '''
    Returns details about given interface.

    CLI Example:

    .. code-block:: bash

        salt '*' ip.get_interface eth0
    '''
    _interfaces = get_interfaces_details()
    for _interface in _interfaces['interfaces']:
        if _interface['connectionid'] == iface:
            return _dict_to_string(_interface)
    return None