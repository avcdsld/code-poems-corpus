def host_status(hostname=None, **kwargs):
    '''
    Check status of a particular host By default
    statuses are returned in a numeric format.

    Parameters:

    hostname
        The hostname to check the status of the service in Nagios.

    numeric
        Turn to false in order to return status in text format
        ('OK' instead of 0, 'Warning' instead of 1 etc)

    :return: status:     'OK', 'Warning', 'Critical' or 'Unknown'

    CLI Example:

    .. code-block:: bash

        salt '*' nagios_rpc.host_status hostname=webserver.domain.com
        salt '*' nagios_rpc.host_status hostname=webserver.domain.com numeric=False
    '''

    if not hostname:
        raise CommandExecutionError('Missing hostname parameter')

    target = 'host'
    numeric = kwargs.get('numeric')
    data = _status_query(target, hostname, enumerate=numeric)

    ret = {'result': data['result']}
    if ret['result']:
        ret['status'] = data.get('json_data', {}).get('data', {}).get(target, {}).get('status',
                                                                                      not numeric and 'Unknown' or 2)
    else:
        ret['error'] = data['error']
    return ret