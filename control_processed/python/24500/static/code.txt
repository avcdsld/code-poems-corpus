def get_pending_domain_join():
    '''
    Determine whether there is a pending domain join action that requires a
    reboot.

    .. versionadded:: 2016.11.0

    Returns:
        bool: ``True`` if there is a pending domain join action, otherwise
        ``False``

    CLI Example:

    .. code-block:: bash

        salt '*' system.get_pending_domain_join
    '''
    base_key = r'SYSTEM\CurrentControlSet\Services\Netlogon'
    avoid_key = r'{0}\AvoidSpnSet'.format(base_key)
    join_key = r'{0}\JoinDomain'.format(base_key)

    # If either the avoid_key or join_key is present,
    # then there is a reboot pending.
    if __utils__['reg.key_exists']('HKLM', avoid_key):
        log.debug('Key exists: %s', avoid_key)
        return True
    else:
        log.debug('Key does not exist: %s', avoid_key)

    if __utils__['reg.key_exists']('HKLM', join_key):
        log.debug('Key exists: %s', join_key)
        return True
    else:
        log.debug('Key does not exist: %s', join_key)

    return False