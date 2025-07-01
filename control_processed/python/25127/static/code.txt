def port_policy_absent(name, sel_type=None, protocol=None, port=None):
    '''
    .. versionadded:: 2019.2.0

    Makes sure an SELinux port policy for a given port, protocol and SELinux context type is absent.

    name
        The protocol and port spec. Can be formatted as ``(tcp|udp)/(port|port-range)``.

    sel_type
        The SELinux Type. Optional; can be used in determining if policy is present,
        ignored by ``semanage port --delete``.

    protocol
        The protocol for the port, ``tcp`` or ``udp``. Required if name is not formatted.

    port
        The port or port range. Required if name is not formatted.
    '''
    ret = {'name': name, 'result': False, 'changes': {}, 'comment': ''}
    old_state = __salt__['selinux.port_get_policy'](
        name=name,
        sel_type=sel_type,
        protocol=protocol,
        port=port, )
    if not old_state:
        ret.update({'result': True,
                    'comment': 'SELinux policy for "{0}" already absent '.format(name) +
                               'with specified sel_type "{0}", protocol "{1}" and port "{2}".'.format(
                                   sel_type, protocol, port)})
        return ret
    if __opts__['test']:
        ret.update({'result': None})
    else:
        delete_ret = __salt__['selinux.port_delete_policy'](
            name=name,
            protocol=protocol,
            port=port, )
        if delete_ret['retcode'] != 0:
            ret.update({'comment': 'Error deleting policy: {0}'.format(delete_ret)})
        else:
            ret.update({'result': True})
            new_state = __salt__['selinux.port_get_policy'](
                name=name,
                sel_type=sel_type,
                protocol=protocol,
                port=port, )
            ret['changes'].update({'old': old_state, 'new': new_state})
    return ret