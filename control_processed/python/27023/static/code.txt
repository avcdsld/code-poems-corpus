def find_interfaces(*args):
    '''
    Returns the bridge to which the interfaces are bond to

    CLI Example:

    .. code-block:: bash

        salt '*' bridge.find_interfaces eth0 [eth1...]
    '''
    brs = _os_dispatch('brshow')
    if not brs:
        return None

    iflist = {}

    for iface in args:
        for br in brs:
            try:  # a bridge may not contain interfaces
                if iface in brs[br]['interfaces']:
                    iflist[iface] = br
            except Exception:
                pass

    return iflist