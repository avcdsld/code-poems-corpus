def disable(states):
    '''
    Disable state runs.

    CLI Example:

    .. code-block:: bash

        salt '*' state.disable highstate

        salt '*' state.disable highstate,test.succeed_without_changes

    .. note::
        To disable a state file from running provide the same name that would
        be passed in a state.sls call.

        salt '*' state.disable bind.config

    '''
    ret = {
        'res': True,
        'msg': ''
    }

    states = salt.utils.args.split_input(states)

    msg = []
    _disabled = __salt__['grains.get']('state_runs_disabled')
    if not isinstance(_disabled, list):
        _disabled = []

    _changed = False
    for _state in states:
        if _state in _disabled:
            msg.append('Info: {0} state already disabled.'.format(_state))
        else:
            msg.append('Info: {0} state disabled.'.format(_state))
            _disabled.append(_state)
            _changed = True

    if _changed:
        __salt__['grains.setval']('state_runs_disabled', _disabled)

    ret['msg'] = '\n'.join(msg)

    # refresh the grains
    __salt__['saltutil.refresh_modules']()

    return ret