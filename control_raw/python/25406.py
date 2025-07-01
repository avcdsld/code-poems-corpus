def __get_subnetwork(vm_):
    '''
    Get configured subnetwork.
    '''
    ex_subnetwork = config.get_cloud_config_value(
        'subnetwork', vm_, __opts__,
        search_global=False)

    return ex_subnetwork