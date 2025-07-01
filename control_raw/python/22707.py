def term_all_jobs():
    '''
    Sends a termination signal (SIGTERM 15) to all currently running jobs

    CLI Example:

    .. code-block:: bash

        salt '*' saltutil.term_all_jobs
    '''
    ret = []
    for data in running():
        ret.append(signal_job(data['jid'], signal.SIGTERM))
    return ret