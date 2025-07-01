def status(Name,
             region=None, key=None, keyid=None, profile=None):
    '''
    Given a trail name describe its properties.

    Returns a dictionary of interesting properties.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_cloudtrail.describe mytrail

    '''

    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        trail = conn.get_trail_status(Name=Name)
        if trail:
            keys = ('IsLogging', 'LatestDeliveryError', 'LatestNotificationError',
                    'LatestDeliveryTime', 'LatestNotificationTime',
                    'StartLoggingTime', 'StopLoggingTime',
                    'LatestCloudWatchLogsDeliveryError',
                    'LatestCloudWatchLogsDeliveryTime',
                    'LatestDigestDeliveryTime', 'LatestDigestDeliveryError',
                    'LatestDeliveryAttemptTime',
                    'LatestNotificationAttemptTime',
                    'LatestNotificationAttemptSucceeded',
                    'LatestDeliveryAttemptSucceeded',
                    'TimeLoggingStarted',
                    'TimeLoggingStopped')
            return {'trail': dict([(k, trail.get(k)) for k in keys])}
        else:
            return {'trail': None}
    except ClientError as e:
        err = __utils__['boto3.get_error'](e)
        if e.response.get('Error', {}).get('Code') == 'TrailNotFoundException':
            return {'trail': None}
        return {'error': __utils__['boto3.get_error'](e)}