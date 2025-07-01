def remove(name, path):
    '''
    Removes installed alternative for defined <name> and <path>
    or fallback to default alternative, if some defined before.

    name
        is the master name for this link group
        (e.g. pager)

    path
        is the location of one of the alternative target files.
        (e.g. /usr/bin/less)
    '''
    ret = {'name': name,
           'path': path,
           'result': True,
           'changes': {},
           'comment': ''}

    isinstalled = __salt__['alternatives.check_exists'](name, path)
    if isinstalled:
        if __opts__['test']:
            ret['comment'] = ('Alternative for {0} will be removed'
                              .format(name))
            ret['result'] = None
            return ret
        __salt__['alternatives.remove'](name, path)
        current = __salt__['alternatives.show_current'](name)
        if current:
            ret['result'] = True
            ret['comment'] = (
                'Alternative for {0} removed. Falling back to path {1}'
            ).format(name, current)
            ret['changes'] = {'path': current}
            return ret

        ret['comment'] = 'Alternative for {0} removed'.format(name)
        ret['changes'] = {}
        return ret

    current = __salt__['alternatives.show_current'](name)
    if current:
        ret['result'] = True
        ret['comment'] = (
            'Alternative for {0} is set to it\'s default path {1}'
        ).format(name, current)
        return ret

    ret['result'] = False
    ret['comment'] = (
        'Alternative for {0} doesn\'t exist'
    ).format(name)

    return ret