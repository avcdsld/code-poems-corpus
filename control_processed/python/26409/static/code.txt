def item(*args, **kwargs):
    '''
    Return one or more grains

    CLI Example:

    .. code-block:: bash

        salt '*' grains.item os
        salt '*' grains.item os osrelease oscodename

    Sanitized CLI Example:

    .. code-block:: bash

        salt '*' grains.item host sanitize=True
    '''
    ret = {}
    default = kwargs.get('default', '')
    delimiter = kwargs.get('delimiter', DEFAULT_TARGET_DELIM)

    try:
        for arg in args:
            ret[arg] = salt.utils.data.traverse_dict_and_list(
                __grains__,
                arg,
                default,
                delimiter)
    except KeyError:
        pass

    if salt.utils.data.is_true(kwargs.get('sanitize')):
        for arg, func in six.iteritems(_SANITIZERS):
            if arg in ret:
                ret[arg] = func(ret[arg])
    return ret