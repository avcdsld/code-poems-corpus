def get_connection(service, module=None, region=None, key=None, keyid=None,
                   profile=None):
    '''
    Return a boto connection for the service.

    .. code-block:: python

        conn = __utils__['boto.get_connection']('ec2', profile='custom_profile')
    '''

    module = module or service

    cxkey, region, key, keyid = _get_profile(service, region, key,
                                             keyid, profile)
    cxkey = cxkey + ':conn3'

    if cxkey in __context__:
        return __context__[cxkey]

    try:
        session = boto3.session.Session(aws_access_key_id=keyid,
                          aws_secret_access_key=key,
                          region_name=region)
        if session is None:
            raise SaltInvocationError('Region "{0}" is not '
                                      'valid.'.format(region))
        conn = session.client(module)
        if conn is None:
            raise SaltInvocationError('Region "{0}" is not '
                                      'valid.'.format(region))
    except boto.exception.NoAuthHandlerFound:
        raise SaltInvocationError('No authentication credentials found when '
                                  'attempting to make boto {0} connection to '
                                  'region "{1}".'.format(service, region))
    __context__[cxkey] = conn
    return conn