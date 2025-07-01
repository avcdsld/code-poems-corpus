def unlock(name,
           zk_hosts=None,  # in case you need to unlock without having run lock (failed execution for example)
           identifier=None,
           max_concurrency=1,
           ephemeral_lease=False,
           profile=None,
           scheme=None,
           username=None,
           password=None,
           default_acl=None):
    '''
    Remove lease from semaphore.
    '''
    ret = {'name': name,
           'changes': {},
           'result': False,
           'comment': ''}
    conn_kwargs = {'profile': profile, 'scheme': scheme,
                   'username': username, 'password': password, 'default_acl': default_acl}

    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'Released lock if it is here'
        return ret

    if identifier is None:
        identifier = __grains__['id']

    unlocked = __salt__['zk_concurrency.unlock'](name,
                                                 zk_hosts=zk_hosts,
                                                 identifier=identifier,
                                                 max_concurrency=max_concurrency,
                                                 ephemeral_lease=ephemeral_lease,
                                                 **conn_kwargs)

    if unlocked:
        ret['result'] = True
    else:
        ret['comment'] = 'Unable to find lease for path {0}'.format(name)

    return ret