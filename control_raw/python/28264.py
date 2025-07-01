def event_source_mapping_exists(UUID=None, EventSourceArn=None,
                                FunctionName=None,
                                region=None, key=None, keyid=None, profile=None):
    '''
    Given an event source mapping ID or an event source ARN and FunctionName,
    check whether the mapping exists.

    Returns True if the given alias exists and returns False if the given
    alias does not exist.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_lambda.alias_exists myfunction myalias

    '''

    desc = describe_event_source_mapping(UUID=UUID,
                                         EventSourceArn=EventSourceArn,
                                         FunctionName=FunctionName,
                                         region=region, key=key,
                                         keyid=keyid, profile=profile)
    if 'error' in desc:
        return desc
    return {'exists': bool(desc.get('event_source_mapping'))}