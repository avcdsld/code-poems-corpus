def deployment_check_existence(name, resource_group, **kwargs):
    '''
    .. versionadded:: 2019.2.0

    Check the existence of a deployment.

    :param name: The name of the deployment to query.

    :param resource_group: The resource group name assigned to the
        deployment.

    CLI Example:

    .. code-block:: bash

        salt-call azurearm_resource.deployment_check_existence testdeploy testgroup

    '''
    result = False
    resconn = __utils__['azurearm.get_client']('resource', **kwargs)
    try:
        result = resconn.deployments.check_existence(
            deployment_name=name,
            resource_group_name=resource_group
        )
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('resource', str(exc), **kwargs)

    return result