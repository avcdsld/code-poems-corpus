def _ensure_exists(name, path=None):
    '''
    Raise an exception if the container does not exist
    '''
    if not exists(name, path=path):
        raise CommandExecutionError(
            'Container \'{0}\' does not exist'.format(name)
        )