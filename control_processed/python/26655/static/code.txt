def _initialize_connection(api_key, app_key):
    '''
    Initialize Datadog connection
    '''
    if api_key is None:
        raise SaltInvocationError('api_key must be specified')
    if app_key is None:
        raise SaltInvocationError('app_key must be specified')
    options = {
        'api_key': api_key,
        'app_key': app_key
    }
    datadog.initialize(**options)