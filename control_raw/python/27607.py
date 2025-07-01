def role_search(auth=None, **kwargs):
    '''
    Search roles

    CLI Example:

    .. code-block:: bash

        salt '*' keystoneng.role_search
        salt '*' keystoneng.role_search name=role1
        salt '*' keystoneng.role_search domain_id=b62e76fbeeff4e8fb77073f591cf211e
    '''
    cloud = get_operator_cloud(auth)
    kwargs = _clean_kwargs(**kwargs)
    return cloud.search_roles(**kwargs)