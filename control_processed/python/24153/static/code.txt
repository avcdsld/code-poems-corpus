def absent(name,
           vhost='/',
           runas=None):
    '''
    Ensure the named policy is absent

    Reference: http://www.rabbitmq.com/ha.html

    name
        The name of the policy to remove
    runas
        Name of the user to run the command as
    '''
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}

    policy_exists = __salt__['rabbitmq.policy_exists'](
        vhost, name, runas=runas)

    if not policy_exists:
        ret['comment'] = 'Policy \'{0} {1}\' is not present.'.format(vhost, name)
        return ret

    if not __opts__['test']:
        result = __salt__['rabbitmq.delete_policy'](vhost, name, runas=runas)
        if 'Error' in result:
            ret['result'] = False
            ret['comment'] = result['Error']
            return ret
        elif 'Deleted' in result:
            ret['comment'] = 'Deleted'

    # If we've reached this far before returning, we have changes.
    ret['changes'] = {'new': '', 'old': name}

    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'Policy \'{0} {1}\' will be removed.'.format(vhost, name)

    return ret