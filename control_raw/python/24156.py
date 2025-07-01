def get_conn():
    '''
    Return a conn object for the passed VM data
    '''
    if __active_provider_name__ in __context__:
        return __context__[__active_provider_name__]
    vm_ = get_configured_provider()
    profile = vm_.pop('profile', None)
    if profile is not None:
        vm_ = __utils__['dictupdate.update'](os_client_config.vendors.get_profile(profile), vm_)
    conn = shade.openstackcloud.OpenStackCloud(cloud_config=None, **vm_)
    if __active_provider_name__ is not None:
        __context__[__active_provider_name__] = conn
    return conn