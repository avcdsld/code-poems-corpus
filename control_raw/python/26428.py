def get_nics(vm_):
    '''
    Return info about the network interfaces of a named vm

    CLI Example:

    .. code-block:: bash

        salt '*' virt.get_nics <vm name>
    '''
    with _get_xapi_session() as xapi:
        nic = {}

        vm_rec = _get_record_by_label(xapi, 'VM', vm_)
        if vm_rec is False:
            return False
        for vif in vm_rec['VIFs']:
            vif_rec = _get_record(xapi, 'VIF', vif)
            nic[vif_rec['MAC']] = {
                'mac': vif_rec['MAC'],
                'device': vif_rec['device'],
                'mtu': vif_rec['MTU']
            }

        return nic