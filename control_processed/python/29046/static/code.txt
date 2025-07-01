def describe_policy_version(policyName, policyVersionId,
             region=None, key=None, keyid=None, profile=None):
    '''
    Given a policy name and version describe its properties.

    Returns a dictionary of interesting properties.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_iot.describe_policy_version mypolicy version

    '''

    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        policy = conn.get_policy_version(policyName=policyName,
                                         policyVersionId=policyVersionId)
        if policy:
            keys = ('policyName', 'policyArn', 'policyDocument',
                    'policyVersionId', 'isDefaultVersion')
            return {'policy': dict([(k, policy.get(k)) for k in keys])}
        else:
            return {'policy': None}
    except ClientError as e:
        err = __utils__['boto3.get_error'](e)
        if e.response.get('Error', {}).get('Code') == 'ResourceNotFoundException':
            return {'policy': None}
        return {'error': __utils__['boto3.get_error'](e)}