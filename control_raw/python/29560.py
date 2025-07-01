def process_read_exception(exc, path, ignore=None):
    '''
    Common code for raising exceptions when reading a file fails

    The ignore argument can be an iterable of integer error codes (or a single
    integer error code) that should be ignored.
    '''
    if ignore is not None:
        if isinstance(ignore, six.integer_types):
            ignore = (ignore,)
    else:
        ignore = ()

    if exc.errno in ignore:
        return

    if exc.errno == errno.ENOENT:
        raise CommandExecutionError('{0} does not exist'.format(path))
    elif exc.errno == errno.EACCES:
        raise CommandExecutionError(
            'Permission denied reading from {0}'.format(path)
        )
    else:
        raise CommandExecutionError(
            'Error {0} encountered reading from {1}: {2}'.format(
                exc.errno, path, exc.strerror
            )
        )