def resource_groups_list(**kwargs):
    '''
    .. versionadded:: 2019.2.0

    List all resource groups within a subscription.

    CLI Example:

    .. code-block:: bash

        salt-call azurearm_resource.resource_groups_list

    '''
    result = {}
    resconn = __utils__['azurearm.get_client']('resource', **kwargs)
    try:
        groups = __utils__['azurearm.paged_object_to_list'](resconn.resource_groups.list())

        for group in groups:
            result[group['name']] = group
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('resource', str(exc), **kwargs)
        result = {'error': str(exc)}

    return result