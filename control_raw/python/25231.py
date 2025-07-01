def get_rich_rules(zone, permanent=True):
    '''
    List rich rules bound to a zone

    .. versionadded:: 2016.11.0

    CLI Example:

    .. code-block:: bash

        salt '*' firewalld.get_rich_rules zone
    '''
    cmd = '--zone={0} --list-rich-rules'.format(zone)

    if permanent:
        cmd += ' --permanent'

    return __firewall_cmd(cmd).splitlines()