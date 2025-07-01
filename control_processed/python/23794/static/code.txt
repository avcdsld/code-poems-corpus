def lv_present(name,
               vgname=None,
               size=None,
               extents=None,
               snapshot=None,
               pv='',
               thinvolume=False,
               thinpool=False,
               force=False,
               **kwargs):
    '''
    Create a new Logical Volume

    name
        The name of the Logical Volume

    vgname
        The name of the Volume Group on which the Logical Volume resides

    size
        The initial size of the Logical Volume

    extents
        The number of logical extents to allocate

    snapshot
        The name of the snapshot

    pv
        The Physical Volume to use

    kwargs
        Any supported options to lvcreate. See
        :mod:`linux_lvm <salt.modules.linux_lvm>` for more details.

    .. versionadded:: to_complete

    thinvolume
        Logical Volume is thinly provisioned

    thinpool
        Logical Volume is a thin pool

    .. versionadded:: 2018.3.0

    force
        Assume yes to all prompts

    '''
    ret = {'changes': {},
           'comment': '',
           'name': name,
           'result': True}

    _snapshot = None

    if snapshot:
        _snapshot = name
        name = snapshot

    if thinvolume:
        lvpath = '/dev/{0}/{1}'.format(vgname.split('/')[0], name)
    else:
        lvpath = '/dev/{0}/{1}'.format(vgname, name)

    if __salt__['lvm.lvdisplay'](lvpath, quiet=True):
        ret['comment'] = 'Logical Volume {0} already present'.format(name)
    elif __opts__['test']:
        ret['comment'] = 'Logical Volume {0} is set to be created'.format(name)
        ret['result'] = None
        return ret
    else:
        changes = __salt__['lvm.lvcreate'](name,
                                           vgname,
                                           size=size,
                                           extents=extents,
                                           snapshot=_snapshot,
                                           pv=pv,
                                           thinvolume=thinvolume,
                                           thinpool=thinpool,
                                           force=force,
                                           **kwargs)

        if __salt__['lvm.lvdisplay'](lvpath):
            ret['comment'] = 'Created Logical Volume {0}'.format(name)
            ret['changes']['created'] = changes
        else:
            ret['comment'] = 'Failed to create Logical Volume {0}. Error: {1}'.format(name, changes)
            ret['result'] = False
    return ret