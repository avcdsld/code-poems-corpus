def enforce_tags(Resource, Tags, region=None, key=None, keyid=None, profile=None):
    '''
    Enforce a given set of tags on a CloudFront resource:  adding, removing, or changing them
    as necessary to ensure the resource's tags are exactly and only those specified.

    Resource
        The ARN of the affected CloudFront resource.

    Tags
        Dict of {'Tag': 'Value', ...} providing the tags to be enforced.

    region
        Region to connect to.

    key
        Secret key to use.

    keyid
        Access key to use.

    profile
        Dict, or pillar key pointing to a dict, containing AWS region/key/keyid.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_cloudfront.enforce_tags Tags='{Owner: Infra, Role: salt_master}' \\
                Resource='arn:aws:cloudfront::012345678012:distribution/ETLNABCDEF123'

    '''
    authargs = {'region': region, 'key': key, 'keyid': keyid, 'profile': profile}
    current = list_tags_for_resource(Resource=Resource, **authargs)
    if current is None:
        log.error('Failed to list tags for CloudFront resource `%s`.', Resource)
        return False
    if current == Tags:  # Short-ciruits save cycles!
        return True
    remove = [k for k in current if k not in Tags]
    removed = untag_resource(Resource=Resource, TagKeys=remove, **authargs)
    if removed is False:
        log.error('Failed to remove tags (%s) from CloudFront resource `%s`.', remove, Resource)
        return False
    add = {k: v for k, v in Tags.items() if current.get(k) != v}
    added = tag_resource(Resource=Resource, Tags=add, **authargs)
    if added is False:
        log.error('Failed to add tags (%s) to CloudFront resource `%s`.', add, Resource)
        return False
    return True