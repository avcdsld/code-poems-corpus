def _get_client(region, key, keyid, profile):
    '''
    Get a boto connection to Data Pipeline.
    '''
    session = _get_session(region, key, keyid, profile)
    if not session:
        log.error("Failed to get datapipeline client.")
        return None

    return session.client('datapipeline')