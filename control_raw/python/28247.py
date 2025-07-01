def delete_function(FunctionName, Qualifier=None, region=None, key=None, keyid=None, profile=None):
    '''
    Given a function name and optional version qualifier, delete it.

    Returns {deleted: true} if the function was deleted and returns
    {deleted: false} if the function was not deleted.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_lambda.delete_function myfunction

    '''

    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        if Qualifier:
            conn.delete_function(
                FunctionName=FunctionName, Qualifier=Qualifier)
        else:
            conn.delete_function(FunctionName=FunctionName)
        return {'deleted': True}
    except ClientError as e:
        return {'deleted': False, 'error': __utils__['boto3.get_error'](e)}