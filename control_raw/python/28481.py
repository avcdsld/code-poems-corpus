def set_mode(iface, mode):
    '''
    List networks on a wireless interface

    CLI Example:

        salt minion iwtools.set_mode wlp3s0 Managed
    '''
    if not _valid_iface(iface):
        raise SaltInvocationError(
            'The interface specified is not valid'
        )

    valid_modes = ('Managed', 'Ad-Hoc', 'Master', 'Repeater', 'Secondary', 'Monitor', 'Auto')
    if mode not in valid_modes:
        raise SaltInvocationError(
            'One of the following modes must be specified: {0}'.format(', '.join(valid_modes))
        )
    __salt__['ip.down'](iface)
    out = __salt__['cmd.run']('iwconfig {0} mode {1}'.format(iface, mode))
    __salt__['ip.up'](iface)

    return mode