def create_api_integration_response(restApiId, resourcePath, httpMethod, statusCode, selectionPattern,
                                    responseParameters=None, responseTemplates=None,
                                    region=None, key=None, keyid=None, profile=None):
    '''
    Creates an integration response for a given method in a given API

    CLI Example:

    .. code-block:: bash

        salt myminion boto_apigateway.create_api_integration_response restApiId resourcePath httpMethod \\
                            statusCode selectionPattern ['{}' ['{}']]

    '''
    try:
        resource = describe_api_resource(restApiId, resourcePath, region=region,
                                         key=key, keyid=keyid, profile=profile).get('resource')
        if resource:
            responseParameters = dict() if responseParameters is None else responseParameters
            responseTemplates = dict() if responseTemplates is None else responseTemplates

            conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
            response = conn.put_integration_response(restApiId=restApiId, resourceId=resource['id'],
                                                     httpMethod=httpMethod, statusCode=statusCode,
                                                     selectionPattern=selectionPattern,
                                                     responseParameters=responseParameters,
                                                     responseTemplates=responseTemplates)
            return {'created': True, 'response': response}
        return {'created': False, 'error': 'no such resource'}
    except ClientError as e:
        return {'created': False, 'error': __utils__['boto3.get_error'](e)}