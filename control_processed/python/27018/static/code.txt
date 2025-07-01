def _bsd_brdel(br):
    '''
    Internal, deletes the bridge
    '''
    ifconfig = _tool_path('ifconfig')
    if not br:
        return False
    return __salt__['cmd.run']('{0} {1} destroy'.format(ifconfig, br),
                               python_shell=False)