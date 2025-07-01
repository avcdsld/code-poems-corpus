def _check_queue(queue, kwargs):
    '''
    Utility function to queue the state run if requested
    and to check for conflicts in currently running states
    '''
    if queue:
        _wait(kwargs.get('__pub_jid'))
    else:
        conflict = running(concurrent=kwargs.get('concurrent', False))
        if conflict:
            __context__['retcode'] = 1
            return conflict