def _is_exposed(minion):
    '''
    Check if the minion is exposed, based on the whitelist and blacklist
    '''
    return salt.utils.stringutils.check_whitelist_blacklist(
        minion,
        whitelist=__opts__['minionfs_whitelist'],
        blacklist=__opts__['minionfs_blacklist']
    )