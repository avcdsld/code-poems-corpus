def match_version(desired, available, cmp_func=None, ignore_epoch=False):
    '''
    Returns the first version of the list of available versions which matches
    the desired version comparison expression, or None if no match is found.
    '''
    oper, version = split_comparison(desired)
    if not oper:
        oper = '=='
    for candidate in available:
        if salt.utils.versions.compare(ver1=candidate,
                                       oper=oper,
                                       ver2=version,
                                       cmp_func=cmp_func,
                                       ignore_epoch=ignore_epoch):
            return candidate
    return None