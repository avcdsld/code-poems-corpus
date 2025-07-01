def updated(name=None, cyg_arch='x86_64', mirrors=None):
    '''
    Make sure all packages are up to date.

    name : None
        No affect, salt fails poorly without the arg available

    cyg_arch : x86_64
        The cygwin architecture to update.
        Current options are x86 and x86_64

    mirrors : None
        List of mirrors to check.
        None will use a default mirror (kernel.org)

    CLI Example:

    .. code-block:: yaml

        rsync:
          cyg.updated:
            - mirrors:
              - http://mirror/without/public/key: ""
              - http://mirror/with/public/key: http://url/of/public/key
    '''
    ret = {'name': 'cyg.updated', 'result': None, 'comment': '', 'changes': {}}

    if cyg_arch not in ['x86', 'x86_64']:
        ret['result'] = False
        ret['comment'] = 'The \'cyg_arch\' argument must\
 be one of \'x86\' or \'x86_64\''
        return ret

    if __opts__['test']:
        ret['comment'] = 'All packages would have been updated'
        return ret

    if not mirrors:
        LOG.warning('No mirror given, using the default.')

    before = __salt__['cyg.list'](cyg_arch=cyg_arch)
    if __salt__['cyg.update'](cyg_arch, mirrors=mirrors):
        after = __salt__['cyg.list'](cyg_arch=cyg_arch)
        differ = DictDiffer(after, before)
        ret['result'] = True
        if differ.same():
            ret['comment'] = 'Nothing to update.'
        else:
            ret['changes']['added'] = list(differ.added())
            ret['changes']['removed'] = list(differ.removed())
            ret['changes']['changed'] = list(differ.changed())
            ret['comment'] = 'All packages successfully updated.'
    else:
        ret['result'] = False
        ret['comment'] = 'Could not update packages.'
    return ret