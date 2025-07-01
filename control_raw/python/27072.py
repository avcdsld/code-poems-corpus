def remove_backup(name):
    '''
    Remove an IIS Configuration backup from the System.

    .. versionadded:: 2017.7.0

    Args:
        name (str): The name of the backup to remove

    Returns:
        bool: True if successful, otherwise False

    CLI Example:

    .. code-block:: bash

        salt '*' win_iis.remove_backup backup_20170209
    '''
    if name not in list_backups():
        log.debug('Backup already removed: %s', name)
        return True

    ps_cmd = ['Remove-WebConfigurationBackup',
              '-Name', "'{0}'".format(name)]

    cmd_ret = _srvmgr(ps_cmd)

    if cmd_ret['retcode'] != 0:
        msg = 'Unable to remove web configuration: {0}\nError: {1}' \
              ''.format(name, cmd_ret['stderr'])
        raise CommandExecutionError(msg)

    return name not in list_backups()