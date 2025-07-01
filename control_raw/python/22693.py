def sync_sdb(saltenv=None, extmod_whitelist=None, extmod_blacklist=None):
    '''
    .. versionadded:: 2015.5.8,2015.8.3

    Sync sdb modules from ``salt://_sdb`` to the minion

    saltenv
        The fileserver environment from which to sync. To sync from more than
        one environment, pass a comma-separated list.

        If not passed, then all environments configured in the :ref:`top files
        <states-top>` will be checked for sdb modules to sync. If no top files
        are found, then the ``base`` environment will be synced.

    refresh : False
        This argument has no affect and is included for consistency with the
        other sync functions.

    extmod_whitelist : None
        comma-seperated list of modules to sync

    extmod_blacklist : None
        comma-seperated list of modules to blacklist based on type

    CLI Example:

    .. code-block:: bash

        salt '*' saltutil.sync_sdb
        salt '*' saltutil.sync_sdb saltenv=dev
        salt '*' saltutil.sync_sdb saltenv=base,dev
    '''
    ret = _sync('sdb', saltenv, extmod_whitelist, extmod_blacklist)
    return ret