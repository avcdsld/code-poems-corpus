def _get_ethercat_interface_info(interface):
    '''
    return details about given ethercat interface
    '''
    base_information = _get_base_interface_info(interface)
    base_information['ethercat'] = {
        'masterid': _load_config(interface.name, ['MasterID'])['MasterID']
    }
    return base_information