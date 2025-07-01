def remove(name):
    '''
    Remove the service <name> from system.
    Returns ``True`` if operation is successful.
    The service will be also stopped.

    name
        the service's name

    CLI Example:

    .. code-block:: bash

        salt '*' service.remove <name>
    '''

    if not enabled(name):
        return False

    svc_path = _service_path(name)
    if not os.path.islink(svc_path):
        log.error('%s is not a symlink: not removed', svc_path)
        return False

    if not stop(name):
        log.error('Failed to stop service %s', name)
        return False
    try:
        os.remove(svc_path)
    except IOError:
        log.error('Unable to remove symlink %s', svc_path)
        return False
    return True