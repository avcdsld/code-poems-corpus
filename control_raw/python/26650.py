def show_lowstate(**kwargs):
    '''
    List out the low data that will be applied to this minion

    CLI Example:

    .. code-block:: bash

        salt '*' state.show_lowstate
    '''
    __opts__['grains'] = __grains__
    opts = salt.utils.state.get_sls_opts(__opts__, **kwargs)
    st_ = salt.client.ssh.state.SSHHighState(
            opts,
            __pillar__,
            __salt__,
            __context__['fileclient'])
    st_.push_active()
    chunks = st_.compile_low_chunks()
    _cleanup_slsmod_low_data(chunks)
    return chunks