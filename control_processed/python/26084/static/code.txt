def unpause(name):
    '''
    Unpauses a container

    name
        Container name or ID


    **RETURN DATA**

    A dictionary will be returned, containing the following keys:

    - ``status`` - A dictionary showing the prior state of the container as
      well as the new state
    - ``result`` - A boolean noting whether or not the action was successful
    - ``comment`` - Only present if the container can not be unpaused


    CLI Example:

    .. code-block:: bash

        salt myminion docker.pause mycontainer
    '''
    orig_state = state(name)
    if orig_state == 'stopped':
        return {'result': False,
                'state': {'old': orig_state, 'new': orig_state},
                'comment': ('Container \'{0}\' is stopped, cannot unpause'
                            .format(name))}
    return _change_state(name, 'unpause', 'running')