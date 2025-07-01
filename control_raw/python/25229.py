def get_sources(zone, permanent=True):
    '''
    List sources bound to a zone

    .. versionadded:: 2016.3.0

    CLI Example:

    .. code-block:: bash

        salt '*' firewalld.get_sources zone
    '''
    cmd = '--zone={0} --list-sources'.format(zone)

    if permanent:
        cmd += ' --permanent'

    return __firewall_cmd(cmd).split()