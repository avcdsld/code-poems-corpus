def topic_present(name, subscriptions=None, attributes=None,
                  region=None, key=None, keyid=None, profile=None):
    '''
    Ensure the SNS topic exists.

    name
        Name of the SNS topic.

    subscriptions
        List of SNS subscriptions.

        Each subscription is a dictionary with a protocol and endpoint key:

        .. code-block:: yaml

            subscriptions:
            - Protocol: https
              Endpoint: https://www.example.com/sns-endpoint
            - Protocol: sqs
              Endpoint: arn:aws:sqs:us-west-2:123456789012:MyQueue

        Additional attributes which may be set on a subscription are:
        - DeliveryPolicy
        - FilterPolicy
        - RawMessageDelivery

        If provided, they should be passed as key/value pairs within the same dictionaries.
        E.g.

        .. code-block:: yaml

            subscriptions:
            - Protocol: sqs
              Endpoint: arn:aws:sqs:us-west-2:123456789012:MyQueue
              RawMessageDelivery: True

    attributes
        Dictionary of attributes to set on the SNS topic
        Valid attribute keys are:
          - Policy:  the JSON serialization of the topic's access control policy
          - DisplayName:  the human-readable name used in the "From" field for notifications
                to email and email-json endpoints
          - DeliveryPolicy:  the JSON serialization of the topic's delivery policy

    region
        Region to connect to.

    key
        Secret key to be used.

    keyid
        Access key to be used.

    profile
        A dict with region, key and keyid, or a pillar key (string)
        that contains a dict with region, key and keyid.
    '''
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}

    something_changed = False
    current = __salt__['boto3_sns.describe_topic'](name, region, key, keyid, profile)
    if current:
        ret['comment'] = 'AWS SNS topic {0} present.'.format(name)
        TopicArn = current['TopicArn']
    else:
        if __opts__['test']:
            ret['comment'] = 'AWS SNS topic {0} would be created.'.format(name)
            ret['result'] = None
            return ret
        else:
            TopicArn = __salt__['boto3_sns.create_topic'](name, region=region, key=key,
                                                          keyid=keyid, profile=profile)
            if TopicArn:
                ret['comment'] = 'AWS SNS topic {0} created with ARN {1}.'.format(name, TopicArn)
                something_changed = True
            else:
                ret['comment'] = 'Failed to create AWS SNS topic {0}'.format(name)
                log.error(ret['comment'])
                ret['result'] = False
                return ret

    ### Update any explicitly defined attributes
    want_attrs = attributes if attributes else {}
    # Freshen these in case we just created it above
    curr_attrs = __salt__['boto3_sns.get_topic_attributes'](TopicArn, region=region, key=key,
                                                            keyid=keyid, profile=profile)
    for attr in ['DisplayName', 'Policy', 'DeliveryPolicy']:
        curr_val = curr_attrs.get(attr)
        want_val = want_attrs.get(attr)
        # Some get default values if not set, so it's not safe to enforce absense if they're
        # not provided at all.  This implies that if you want to clear a value, you must explicitly
        # set it to an empty string.
        if want_val is None:
            continue
        if _json_objs_equal(want_val, curr_val):
            continue
        if __opts__['test']:
            ret['comment'] += '  Attribute {} would be updated on topic {}.'.format(attr, TopicArn)
            ret['result'] = None
            continue
        want_val = want_val if isinstance(want_val,
                                          six.string_types) else salt.utils.json.dumps(want_val)
        if __salt__['boto3_sns.set_topic_attributes'](TopicArn, attr, want_val, region=region,
                                                      key=key, keyid=keyid, profile=profile):
            ret['comment'] += '  Attribute {0} set to {1} on topic {2}.'.format(attr, want_val,
                                                                                   TopicArn)
            something_changed = True
        else:
            ret['comment'] += '  Failed to update {0} on topic {1}.'.format(attr, TopicArn)
            ret['result'] = False
            return ret

    ### Add / remove subscriptions
    mutable_attrs = ('DeliveryPolicy', 'FilterPolicy', 'RawMessageDelivery')
    want_subs = subscriptions if subscriptions else []
    want_subs = [{k: v for k, v in c.items() if k in ('Protocol', 'Endpoint') or k in mutable_attrs}
                 for c in want_subs]
    curr_subs = current.get('Subscriptions', [])
    subscribe = []
    unsubscribe = []
    want_obfuscated = []
    for sub in want_subs:
        # If the subscription contains inline digest auth, AWS will obfuscate the password
        # with '****'.  Thus we need to do the same with ours to permit 1-to-1 comparison.
        # Example: https://user:****@my.endpoiint.com/foo/bar
        endpoint = sub['Endpoint']
        matches = re.search(r'http[s]?://(?P<user>\w+):(?P<pass>\w+)@', endpoint)
        if matches is not None:
            sub['Endpoint'] = endpoint.replace(':' + matches.groupdict()['pass'], ':****')
        want_obfuscated += [{'Protocol': sub['Protocol'], 'Endpoint': sub['Endpoint']}]
        if sub not in curr_subs:
            sub['obfuscated'] = sub['Endpoint']
            sub['Endpoint'] = endpoint   # Set it back to the unobfuscated value.
            subscribe += [sub]
    for sub in curr_subs:
        if {'Protocol': sub['Protocol'], 'Endpoint': sub['Endpoint']} not in want_obfuscated:
            if sub['SubscriptionArn'].startswith('arn:aws:sns:'):
                unsubscribe += [sub['SubscriptionArn']]
    for sub in subscribe:
        ret = _create_or_update_subscription(ret, sub, curr_subs, mutable_attrs, TopicArn,
                                                region, key, keyid, profile)
        if ret.pop('something_changed', False) is True:
            something_changed = True
    for sub in unsubscribe:
        if __opts__['test']:
            msg = '  Subscription {} would be removed from topic {}.'.format(sub, TopicArn)
            ret['comment'] += msg
            ret['result'] = None
            continue
        unsubbed = __salt__['boto3_sns.unsubscribe'](sub, region=region, key=key, keyid=keyid,
                                                     profile=profile)
        if unsubbed:
            ret['comment'] += '  Subscription {0} removed from topic {1}.'.format(sub, TopicArn)
            something_changed = True
        else:
            msg = '  Failed to remove subscription {0} from topic {1}.'.format(sub, TopicArn)
            ret['comment'] += msg
            ret['result'] = False
            return ret
    if something_changed:
        ret['changes']['old'] = current
        ret['changes']['new'] = __salt__['boto3_sns.describe_topic'](name, region, key, keyid, profile)
    return ret