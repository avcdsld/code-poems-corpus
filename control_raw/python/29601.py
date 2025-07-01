def update_connector_c_pool(name, server=None, **kwargs):
    '''
    Update a connection pool
    '''
    if 'transactionSupport' in kwargs and kwargs['transactionSupport'] not in (
               'XATransaction',
               'LocalTransaction',
               'NoTransaction'
       ):
        raise CommandExecutionError('Invalid transaction support')
    return _update_element(name, 'resources/connector-connection-pool', kwargs, server)