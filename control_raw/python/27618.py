def endpoint_list(auth=None, **kwargs):
    '''
    List endpoints

    CLI Example:

    .. code-block:: bash

        salt '*' keystoneng.endpoint_list
    '''
    cloud = get_operator_cloud(auth)
    kwargs = _clean_kwargs(**kwargs)
    return cloud.list_endpoints(**kwargs)