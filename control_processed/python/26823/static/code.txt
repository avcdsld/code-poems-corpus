def present(name, auth=None, **kwargs):
    '''
    Ensure domain exists and is up-to-date

    name
        Name of the domain

    enabled
        Boolean to control if domain is enabled

    description
        An arbitrary description of the domain
    '''
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''}

    kwargs = __utils__['args.clean_kwargs'](**kwargs)

    __salt__['keystoneng.setup_clouds'](auth)

    domain = __salt__['keystoneng.domain_get'](name=name)

    if not domain:
        if __opts__['test']:
            ret['result'] = None
            ret['changes'] = kwargs
            ret['comment'] = 'Domain {} will be created.'.format(name)
            return ret

        kwargs['name'] = name
        domain = __salt__['keystoneng.domain_create'](**kwargs)
        ret['changes'] = domain
        ret['comment'] = 'Created domain'
        return ret

    changes = __salt__['keystoneng.compare_changes'](domain, **kwargs)
    if changes:
        if __opts__['test']:
            ret['result'] = None
            ret['changes'] = changes
            ret['comment'] = 'Domain {} will be updated.'.format(name)
            return ret

        kwargs['domain_id'] = domain.id
        __salt__['keystoneng.domain_update'](**kwargs)
        ret['changes'].update(changes)
        ret['comment'] = 'Updated domain'

    return ret