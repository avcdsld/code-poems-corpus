def history(zpool=None, internal=False, verbose=False):
    '''
    .. versionadded:: 2016.3.0

    Displays the command history of the specified pools, or all pools if no
    pool is specified

    zpool : string
        Optional storage pool

    internal : boolean
        Toggle display of internally logged ZFS events

    verbose : boolean
        Toggle display of the user name, the hostname, and the zone in which
        the operation was performed

    CLI Example:

    .. code-block:: bash

        salt '*' zpool.upgrade myzpool

    '''
    ret = OrderedDict()

    ## Configure pool
    # NOTE: initialize the defaults
    flags = []

    # NOTE: set extra config
    if verbose:
        flags.append('-l')
    if internal:
        flags.append('-i')

    ## Lookup history
    res = __salt__['cmd.run_all'](
        __utils__['zfs.zpool_command'](
            command='history',
            flags=flags,
            target=zpool,
        ),
        python_shell=False,
    )

    if res['retcode'] != 0:
        return __utils__['zfs.parse_command_result'](res)
    else:
        pool = 'unknown'
        for line in res['stdout'].splitlines():
            if line.startswith('History for'):
                pool = line[13:-2]
                ret[pool] = OrderedDict()
            else:
                if line == '':
                    continue
                log_timestamp = line[0:19]
                log_command = line[20:]
                ret[pool][log_timestamp] = log_command

    return ret