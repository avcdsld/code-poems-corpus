def low(data, queue=False, **kwargs):
    '''
    Execute a single low data call

    This function is mostly intended for testing the state system and is not
    likely to be needed in everyday usage.

    CLI Example:

    .. code-block:: bash

        salt '*' state.low '{"state": "pkg", "fun": "installed", "name": "vi"}'
    '''
    conflict = _check_queue(queue, kwargs)
    if conflict is not None:
        return conflict
    try:
        st_ = salt.state.State(__opts__, proxy=__proxy__)
    except NameError:
        st_ = salt.state.State(__opts__)
    err = st_.verify_data(data)
    if err:
        __context__['retcode'] = salt.defaults.exitcodes.EX_STATE_COMPILER_ERROR
        return err
    ret = st_.call(data)
    if isinstance(ret, list):
        __context__['retcode'] = salt.defaults.exitcodes.EX_STATE_COMPILER_ERROR
    if __utils__['state.check_result'](ret):
        __context__['retcode'] = salt.defaults.exitcodes.EX_STATE_FAILURE
    return ret