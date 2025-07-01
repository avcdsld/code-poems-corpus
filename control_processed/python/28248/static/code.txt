def describe_function(FunctionName, region=None, key=None,
                      keyid=None, profile=None):
    '''
    Given a function name describe its properties.

    Returns a dictionary of interesting properties.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_lambda.describe_function myfunction

    '''

    try:
        func = _find_function(FunctionName,
                              region=region, key=key, keyid=keyid, profile=profile)
        if func:
            keys = ('FunctionName', 'Runtime', 'Role', 'Handler', 'CodeSha256',
                    'CodeSize', 'Description', 'Timeout', 'MemorySize',
                    'FunctionArn', 'LastModified', 'VpcConfig', 'Environment')
            return {'function': dict([(k, func.get(k)) for k in keys])}
        else:
            return {'function': None}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}