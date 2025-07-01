def describe_api_deployments(restApiId, region=None, key=None, keyid=None, profile=None):
    '''
    Gets information about the defined API Deployments.  Return list of api deployments.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_apigateway.describe_api_deployments restApiId

    '''
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        deployments = []
        _deployments = conn.get_deployments(restApiId=restApiId)

        while True:
            if _deployments:
                deployments = deployments + _deployments['items']
                if 'position' not in _deployments:
                    break
                _deployments = conn.get_deployments(restApiId=restApiId, position=_deployments['position'])

        return {'deployments': [_convert_datetime_str(deployment) for deployment in deployments]}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}