def _cmd(jail=None):
    '''
    Return full path to service command

    .. versionchanged:: 2016.3.4

    Support for jail (representing jid or jail name) keyword argument in kwargs
    '''
    service = salt.utils.path.which('service')
    if not service:
        raise CommandNotFoundError('\'service\' command not found')
    if jail:
        jexec = salt.utils.path.which('jexec')
        if not jexec:
            raise CommandNotFoundError('\'jexec\' command not found')
        service = '{0} {1} {2}'.format(jexec, jail, service)
    return service