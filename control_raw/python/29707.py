def get_distribution(name, region=None, key=None, keyid=None, profile=None):
    '''
    Get information about a CloudFront distribution (configuration, tags) with a given name.

    name
        Name of the CloudFront distribution

    region
        Region to connect to

    key
        Secret key to use

    keyid
        Access key to use

    profile
        A dict with region, key, and keyid,
        or a pillar key (string) that contains such a dict.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_cloudfront.get_distribution name=mydistribution profile=awsprofile

    '''
    distribution = _cache_id(
        'cloudfront',
        sub_resource=name,
        region=region,
        key=key,
        keyid=keyid,
        profile=profile,
    )
    if distribution:
        return {'result': distribution}

    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        for _, dist in _list_distributions(
            conn,
            name=name,
            region=region,
            key=key,
            keyid=keyid,
            profile=profile,
        ):
            # _list_distributions should only return the one distribution
            # that we want (with the given name).
            # In case of multiple distributions with the same name tag,
            # our use of caching means list_distributions will just
            # return the first one over and over again,
            # so only the first result is useful.
            if distribution is not None:
                msg = 'More than one distribution found with name {0}'
                return {'error': msg.format(name)}
            distribution = dist
    except botocore.exceptions.ClientError as err:
        return {'error': __utils__['boto3.get_error'](err)}
    if not distribution:
        return {'result': None}

    _cache_id(
        'cloudfront',
        sub_resource=name,
        resource_id=distribution,
        region=region,
        key=key,
        keyid=keyid,
        profile=profile,
    )
    return {'result': distribution}