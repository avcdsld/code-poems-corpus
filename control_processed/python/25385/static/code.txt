def get_client(client_type, **kwargs):
    '''
    Dynamically load the selected client and return a management client object
    '''
    client_map = {'compute': 'ComputeManagement',
                  'authorization': 'AuthorizationManagement',
                  'dns': 'DnsManagement',
                  'storage': 'StorageManagement',
                  'managementlock': 'ManagementLock',
                  'monitor': 'MonitorManagement',
                  'network': 'NetworkManagement',
                  'policy': 'Policy',
                  'resource': 'ResourceManagement',
                  'subscription': 'Subscription',
                  'web': 'WebSiteManagement'}

    if client_type not in client_map:
        raise SaltSystemExit(
            msg='The Azure ARM client_type {0} specified can not be found.'.format(
                client_type)
        )

    map_value = client_map[client_type]

    if client_type in ['policy', 'subscription']:
        module_name = 'resource'
    elif client_type in ['managementlock']:
        module_name = 'resource.locks'
    else:
        module_name = client_type

    try:
        client_module = importlib.import_module('azure.mgmt.'+module_name)
        # pylint: disable=invalid-name
        Client = getattr(client_module,
                         '{0}Client'.format(map_value))
    except ImportError:
        raise sys.exit(
                  'The azure {0} client is not available.'.format(client_type)
        )

    credentials, subscription_id, cloud_env = _determine_auth(**kwargs)

    if client_type == 'subscription':
        client = Client(
            credentials=credentials,
            base_url=cloud_env.endpoints.resource_manager,
        )
    else:
        client = Client(
            credentials=credentials,
            subscription_id=subscription_id,
            base_url=cloud_env.endpoints.resource_manager,
        )

    client.config.add_user_agent('Salt/{0}'.format(salt.version.__version__))

    return client