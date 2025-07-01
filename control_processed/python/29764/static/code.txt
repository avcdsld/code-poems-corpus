def flush(name, family='ipv4', **kwargs):
    '''
    .. versionadded:: 2014.7.0

    Flush current ipset set

    family
        Networking family, either ipv4 or ipv6

    '''
    ret = {'name': name,
           'changes': {},
           'result': None,
           'comment': ''}

    set_check = __salt__['ipset.check_set'](name)
    if set_check is False:
        ret['result'] = False
        ret['comment'] = ('ipset set {0} does not exist for {1}'
                          .format(name, family))
        return ret

    if __opts__['test']:
        ret['comment'] = 'ipset entries in set {0} for {1} would be flushed'.format(
            name,
            family)
        return ret
    if __salt__['ipset.flush'](name, family):
        ret['changes'] = {'locale': name}
        ret['result'] = True
        ret['comment'] = 'Flushed ipset entries from set {0} for {1}'.format(
            name,
            family
        )
        return ret
    else:
        ret['result'] = False
        ret['comment'] = 'Failed to flush ipset entries from set {0} for {1}' \
                         ''.format(name, family)
        return ret