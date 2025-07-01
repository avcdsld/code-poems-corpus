def list_(saltenv='base', test=None):
    '''
    List currently configured reactors

    CLI Example:

    .. code-block:: bash

        salt-run reactor.list
    '''
    sevent = salt.utils.event.get_event(
            'master',
            __opts__['sock_dir'],
            __opts__['transport'],
            opts=__opts__,
            listen=True)

    master_key = salt.utils.master.get_master_key('root', __opts__)

    __jid_event__.fire_event({'key': master_key}, 'salt/reactors/manage/list')

    results = sevent.get_event(wait=30, tag='salt/reactors/manage/list-results')
    reactors = results['reactors']
    return reactors