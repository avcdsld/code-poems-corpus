def absent(name, exports='/etc/exports'):
    '''
    Ensure that the named path is not exported

    name
        The export path to remove
    '''

    path = name
    ret = {'name': name,
           'changes': {},
           'result': None,
           'comment': ''}

    old = __salt__['nfs3.list_exports'](exports)
    if path in old:
        if __opts__['test']:
            ret['comment'] = 'Export {0} would be removed'.format(path)
            ret['changes'][path] = old[path]
            ret['result'] = None
            return ret

        __salt__['nfs3.del_export'](exports, path)
        try_reload = __salt__['nfs3.reload_exports']()
        if not try_reload['result']:
            ret['comment'] = try_reload['stderr']
        else:
            ret['comment'] = 'Export {0} removed'.format(path)

        ret['result'] = try_reload['result']
        ret['changes'][path] = old[path]
    else:
        ret['comment'] = 'Export {0} already absent'.format(path)
        ret['result'] = True

    return ret