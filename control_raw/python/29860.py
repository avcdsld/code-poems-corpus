def validate_user(user,
                  device,
                  token):
    '''
    Send a message to a Pushover user or group.
    :param user:        The user or group name, either will work.
    :param device:      The device for the user.
    :param token:       The PushOver token.
    '''
    res = {
            'message': 'User key is invalid',
            'result': False
           }

    parameters = dict()
    parameters['user'] = user
    parameters['token'] = token
    if device:
        parameters['device'] = device

    response = query(function='validate_user',
                     method='POST',
                     header_dict={'Content-Type': 'application/x-www-form-urlencoded'},
                     data=_urlencode(parameters))

    if response['res']:
        if 'message' in response:
            _message = response.get('message', '')
            if 'status' in _message:
                if _message.get('dict', {}).get('status', None) == 1:
                    res['result'] = True
                    res['message'] = 'User key is valid.'
                else:
                    res['result'] = False
                    res['message'] = ''.join(_message.get('dict', {}).get('errors'))
    return res