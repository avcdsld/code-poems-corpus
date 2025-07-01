def info():
    '''
    Return configuration and status information about the marathon instance.

    CLI Example:

    .. code-block:: bash

        salt marathon-minion-id marathon.info
    '''
    response = salt.utils.http.query(
        "{0}/v2/info".format(_base_url()),
        decode_type='json',
        decode=True,
    )
    return response['dict']