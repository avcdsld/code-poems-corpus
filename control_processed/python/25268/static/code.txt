def _get_dvs_infrastructure_traffic_resources(dvs_name,
                                              dvs_infra_traffic_ress):
    '''
    Returns a list of dict representations of the DVS infrastructure traffic
    resource

    dvs_name
        The name of the DVS

    dvs_infra_traffic_ress
        The DVS infrastructure traffic resources
    '''
    log.trace('Building the dicts of the DVS \'%s\' infrastructure '
              'traffic resources', dvs_name)
    res_dicts = []
    for res in dvs_infra_traffic_ress:
        res_dict = {'key': res.key,
                    'limit': res.allocationInfo.limit,
                    'reservation': res.allocationInfo.reservation}
        if res.allocationInfo.shares:
            res_dict.update({'num_shares': res.allocationInfo.shares.shares,
                             'share_level': res.allocationInfo.shares.level})
        res_dicts.append(res_dict)
    return res_dicts