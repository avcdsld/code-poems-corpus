def cancel_commit(jid):
    '''
    .. versionadded:: 2019.2.0

    Cancel a commit scheduled to be executed via the ``commit_in`` and
    ``commit_at`` arguments from the
    :py:func:`net.load_template <salt.modules.napalm_network.load_template>` or
    :py:func:`net.load_config <salt.modules.napalm_network.load_config>`
    execution functions. The commit ID is displayed when the commit is scheduled
    via the functions named above.

    CLI Example:

    .. code-block:: bash

        salt '*' net.cancel_commit 20180726083540640360
    '''
    job_name = '__napalm_commit_{}'.format(jid)
    removed = __salt__['schedule.delete'](job_name)
    if removed['result']:
        saved = __salt__['schedule.save']()
        removed['comment'] = 'Commit #{jid} cancelled.'.format(jid=jid)
    else:
        removed['comment'] = 'Unable to find commit #{jid}.'.format(jid=jid)
    return removed