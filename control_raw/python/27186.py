def show_coalesce(devname):
    '''
    Queries the specified network device for coalescing information

    CLI Example:

    .. code-block:: bash

        salt '*' ethtool.show_coalesce <devname>
    '''

    try:
        coalesce = ethtool.get_coalesce(devname)
    except IOError:
        log.error('Interrupt coalescing not supported on %s', devname)
        return 'Not supported'

    ret = {}
    for key, value in coalesce.items():
        ret[ethtool_coalesce_remap[key]] = coalesce[key]

    return ret