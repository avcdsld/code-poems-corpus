def _lookup_vultrid(which_key, availkey, keyname):
    '''
    Helper function to retrieve a Vultr ID
    '''
    if DETAILS == {}:
        _cache_provider_details()

    which_key = six.text_type(which_key)
    try:
        return DETAILS[availkey][which_key][keyname]
    except KeyError:
        return False