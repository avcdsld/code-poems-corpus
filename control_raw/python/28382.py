def boot_device(name='default', **kwargs):
    '''
    Request power state change

    name = ``default``
        * network -- Request network boot
        * hd -- Boot from hard drive
        * safe -- Boot from hard drive, requesting 'safe mode'
        * optical -- boot from CD/DVD/BD drive
        * setup -- Boot into setup utility
        * default -- remove any IPMI directed boot device request

    kwargs
        - api_host=localhost
        - api_user=admin
        - api_pass=
        - api_port=623
        - api_kg=None
    '''
    ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}
    org = __salt__['ipmi.get_bootdev'](**kwargs)
    if 'bootdev' in org:
        org = org['bootdev']

    if org == name:
        ret['result'] = True
        ret['comment'] = 'system already in this state'
        return ret

    if __opts__['test']:
        ret['comment'] = 'would change boot device'
        ret['result'] = None
        ret['changes'] = {'old': org, 'new': name}
        return ret

    outdddd = __salt__['ipmi.set_bootdev'](bootdev=name, **kwargs)
    ret['comment'] = 'changed boot device'
    ret['result'] = True
    ret['changes'] = {'old': org, 'new': name}
    return ret