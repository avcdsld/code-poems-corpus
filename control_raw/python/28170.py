def _get_cloud_environment():
    '''
    Get the cloud environment object.
    '''
    cloud_environment = config.get_cloud_config_value(
                            'cloud_environment',
                            get_configured_provider(), __opts__, search_global=False
                        )
    try:
        cloud_env_module = importlib.import_module('msrestazure.azure_cloud')
        cloud_env = getattr(cloud_env_module, cloud_environment or 'AZURE_PUBLIC_CLOUD')
    except (AttributeError, ImportError):
        raise SaltCloudSystemExit(
            'The azure {0} cloud environment is not available.'.format(cloud_environment)
        )

    return cloud_env