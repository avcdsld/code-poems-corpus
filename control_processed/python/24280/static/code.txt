def get_all():
    '''
    Return all available boot services

    CLI Example:

    .. code-block:: bash

        salt '*' service.get_all
    '''
    (enabled_services, disabled_services) = _get_service_list(include_enabled=True,
                                                              include_disabled=True)
    enabled_services.update(dict([(s, []) for s in disabled_services]))
    return odict.OrderedDict(enabled_services)