def pv_absent(name):
    '''
    Ensure that a Physical Device is not being used by lvm

    name
        The device name to initialize.
    '''
    ret = {'changes': {},
           'comment': '',
           'name': name,
           'result': True}

    if not __salt__['lvm.pvdisplay'](name, quiet=True):
        ret['comment'] = 'Physical Volume {0} does not exist'.format(name)
    elif __opts__['test']:
        ret['comment'] = 'Physical Volume {0} is set to be removed'.format(name)
        ret['result'] = None
        return ret
    else:
        changes = __salt__['lvm.pvremove'](name)

        if __salt__['lvm.pvdisplay'](name, quiet=True):
            ret['comment'] = 'Failed to remove Physical Volume {0}'.format(name)
            ret['result'] = False
        else:
            ret['comment'] = 'Removed Physical Volume {0}'.format(name)
            ret['changes']['removed'] = changes
    return ret