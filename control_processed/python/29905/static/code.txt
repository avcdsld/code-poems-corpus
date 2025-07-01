def add_subgids(name, first=100000, last=110000):
    '''
    Add a range of subordinate gids to the user

    name
        User to modify

    first
        Begin of the range

    last
        End of the range

    CLI Examples:

    .. code-block:: bash

        salt '*' user.add_subgids foo
        salt '*' user.add_subgids foo first=105000
        salt '*' user.add_subgids foo first=600000000 last=600100000
    '''
    if __grains__['kernel'] != 'Linux':
        log.warning("'subgids' are only supported on GNU/Linux hosts.")

    return __salt__['cmd.run'](['usermod', '-w', '-'.join(str(x) for x in (first, last)), name])