def _post_message(user,
                  device,
                  message,
                  title,
                  priority,
                  expire,
                  retry,
                  sound,
                  api_version=1,
                  token=None):
    '''
    Send a message to a Pushover user or group.
    :param user:        The user or group to send to, must be key of user or group not email address.
    :param message:     The message to send to the PushOver user or group.
    :param title:       Specify who the message is from.
    :param priority     The priority of the message, defaults to 0.
    :param api_version: The PushOver API version, if not specified in the configuration.
    :param notify:      Whether to notify the room, default: False.
    :param token:       The PushOver token, if not specified in the configuration.
    :return:            Boolean if message was sent successfully.
    '''

    user_validate = salt.utils.pushover.validate_user(user, device, token)
    if not user_validate['result']:
        return user_validate

    parameters = dict()
    parameters['user'] = user
    parameters['device'] = device
    parameters['token'] = token
    parameters['title'] = title
    parameters['priority'] = priority
    parameters['expire'] = expire
    parameters['retry'] = retry
    parameters['message'] = message

    if sound:
        sound_validate = salt.utils.pushover.validate_sound(sound, token)
        if sound_validate['res']:
            parameters['sound'] = sound

    result = salt.utils.pushover.query(function='message',
                                       method='POST',
                                       header_dict={'Content-Type': 'application/x-www-form-urlencoded'},
                                       data=_urlencode(parameters),
                                       opts=__opts__)

    return result