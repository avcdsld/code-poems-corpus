def describe_api_integration_response(restApiId, resourcePath, httpMethod, statusCode,
                                      region=None, key=None, keyid=None, profile=None):
    '''
    Get an integration response for a given method in a given API

    CLI Example:

    .. code-block:: bash

        salt myminion boto_apigateway.describe_api_integration_response restApiId resourcePath httpMethod statusCode

    '''
    try:
        resource = describe_api_resource(restApiId, resourcePath, region=region,
                                         key=key, keyid=keyid, profile=profile).get('resource')
        if resource:
            conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
            response = conn.get_integration_response(restApiId=restApiId, resourceId=resource['id'],
                                                     httpMethod=httpMethod, statusCode=statusCode)
            return {'response': _convert_datetime_str(response)}
        return {'error': 'no such resource'}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}