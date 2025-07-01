def mod_list(only_persist=False):
    '''
    Return a list of the loaded module names

    CLI Example:

    .. code-block:: bash

        salt '*' kmod.mod_list
    '''
    mods = set()
    if only_persist:
        if not _get_persistent_modules():
            return mods
        for mod in _get_persistent_modules():
            mods.add(mod)
    else:
        for mod in lsmod():
            mods.add(mod['module'])
    return sorted(list(mods))