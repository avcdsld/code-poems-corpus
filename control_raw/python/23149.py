def _get_cron_cmdstr(path, user=None):
    '''
    Returns a format string, to be used to build a crontab command.
    '''
    if user:
        cmd = 'crontab -u {0}'.format(user)
    else:
        cmd = 'crontab'
    return '{0} {1}'.format(cmd, path)