def create_function(FunctionName, Runtime, Role, Handler, ZipFile=None,
                    S3Bucket=None, S3Key=None, S3ObjectVersion=None,
                    Description="", Timeout=3, MemorySize=128, Publish=False,
                    WaitForRole=False, RoleRetries=5,
                    region=None, key=None, keyid=None, profile=None,
                    VpcConfig=None, Environment=None):
    '''
    .. versionadded:: 2017.7.0

    Given a valid config, create a function.

    Environment
        The parent object that contains your environment's configuration
        settings. This is a dictionary of the form:

        .. code-block:: python

            {
                'Variables': {
                    'VariableName': 'VariableValue'
                }
            }

    Returns ``{'created': True}`` if the function was created and ``{created:
    False}`` if the function was not created.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_lamba.create_function my_function python2.7 my_role my_file.my_function my_function.zip
        salt myminion boto_lamba.create_function my_function python2.7 my_role my_file.my_function salt://files/my_function.zip

    '''

    role_arn = _get_role_arn(Role, region=region, key=key,
                             keyid=keyid, profile=profile)
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        if ZipFile:
            if S3Bucket or S3Key or S3ObjectVersion:
                raise SaltInvocationError('Either ZipFile must be specified, or '
                                          'S3Bucket and S3Key must be provided.')
            if '://' in ZipFile:  # Looks like a remote URL to me...
                dlZipFile = __salt__['cp.cache_file'](path=ZipFile)
                if dlZipFile is False:
                    ret['result'] = False
                    ret['comment'] = 'Failed to cache ZipFile `{0}`.'.format(ZipFile)
                    return ret
                ZipFile = dlZipFile
            code = {
                'ZipFile': _filedata(ZipFile),
            }
        else:
            if not S3Bucket or not S3Key:
                raise SaltInvocationError('Either ZipFile must be specified, or '
                                          'S3Bucket and S3Key must be provided.')
            code = {
                'S3Bucket': S3Bucket,
                'S3Key': S3Key,
            }
            if S3ObjectVersion:
                code['S3ObjectVersion'] = S3ObjectVersion
        kwargs = {}
        if VpcConfig is not None:
            kwargs['VpcConfig'] = _resolve_vpcconfig(VpcConfig, region=region, key=key, keyid=keyid, profile=profile)
        if Environment is not None:
            kwargs['Environment'] = Environment
        if WaitForRole:
            retrycount = RoleRetries
        else:
            retrycount = 1
        for retry in range(retrycount, 0, -1):
            try:
                func = conn.create_function(FunctionName=FunctionName, Runtime=Runtime, Role=role_arn, Handler=Handler,
                                            Code=code, Description=Description, Timeout=Timeout, MemorySize=MemorySize,
                                            Publish=Publish, **kwargs)
            except ClientError as e:
                if retry > 1 and e.response.get('Error', {}).get('Code') == 'InvalidParameterValueException':
                    log.info(
                        'Function not created but IAM role may not have propagated, will retry')
                    # exponential backoff
                    time.sleep((2 ** (RoleRetries - retry)) +
                               (random.randint(0, 1000) / 1000))
                    continue
                else:
                    raise
            else:
                break
        if func:
            log.info('The newly created function name is %s', func['FunctionName'])

            return {'created': True, 'name': func['FunctionName']}
        else:
            log.warning('Function was not created')
            return {'created': False}
    except ClientError as e:
        return {'created': False, 'error': __utils__['boto3.get_error'](e)}