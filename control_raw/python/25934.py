def unlock_file(filename):
    '''
    Unlock a locked file

    Note that these locks are only recognized by Salt Cloud, and not other
    programs or platforms.
    '''
    log.trace('Removing lock for %s', filename)
    lock = filename + '.lock'
    try:
        os.remove(lock)
    except OSError as exc:
        log.trace('Unable to remove lock for %s: %s', filename, exc)