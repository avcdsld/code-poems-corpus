def missing(name, limit=''):
    '''
    The inverse of service.available.
    Return True if the named service is not available.  Use the ``limit`` param to
    restrict results to services of that type.

    CLI Examples:

    .. code-block:: bash

        salt '*' service.missing sshd
        salt '*' service.missing sshd limit=upstart
        salt '*' service.missing sshd limit=sysvinit
    '''
    if limit == 'upstart':
        return not _service_is_upstart(name)
    elif limit == 'sysvinit':
        return not _service_is_sysv(name)
    else:
        if _service_is_upstart(name) or _service_is_sysv(name):
            return False
        else:
            return True