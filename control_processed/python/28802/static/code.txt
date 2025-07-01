def has_flag(conf, atom, flag):
    '''
    Verify if the given package or DEPEND atom has the given flag.
    Warning: This only works if the configuration files tree is in the correct
    format (the one enforced by enforce_nice_config)

    CLI Example:

    .. code-block:: bash

        salt '*' portage_config.has_flag license salt Apache-2.0
    '''
    if flag in get_flags_from_package_conf(conf, atom):
        return True
    return False