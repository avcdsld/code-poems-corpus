def profile_(profile, names, vm_overrides=None, opts=None, **kwargs):
    '''
    Spin up an instance using Salt Cloud

    CLI Example:

    .. code-block:: bash

        salt minionname cloud.profile my-gce-config myinstance
    '''
    client = _get_client()
    if isinstance(opts, dict):
        client.opts.update(opts)
    info = client.profile(profile, names, vm_overrides=vm_overrides, **kwargs)
    return info