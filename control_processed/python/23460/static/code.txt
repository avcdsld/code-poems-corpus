def _get_resource_id(resource, name, region=None, key=None,
                     keyid=None, profile=None):
    '''
    Get an AWS id for a VPC resource by type and name.
    '''

    _id = _cache_id(name, sub_resource=resource,
                    region=region, key=key,
                    keyid=keyid, profile=profile)
    if _id:
        return _id

    r = _get_resource(resource, name=name, region=region, key=key,
                      keyid=keyid, profile=profile)

    if r:
        return r.id