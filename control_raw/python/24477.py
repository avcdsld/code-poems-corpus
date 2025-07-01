def _post_message(channel,
                  message,
                  username,
                  as_user,
                  api_key=None):
    '''
    Send a message to a Slack room.
    :param channel:     The room name.
    :param message:     The message to send to the Slack room.
    :param username:    Specify who the message is from.
    :param as_user:     Sets the profile picture which have been added through Slack itself.
    :param api_key:     The Slack api key, if not specified in the configuration.
    :param api_version: The Slack api version, if not specified in the configuration.
    :return:            Boolean if message was sent successfully.
    '''

    parameters = dict()
    parameters['channel'] = channel
    parameters['username'] = username
    parameters['as_user'] = as_user
    parameters['text'] = '```' + message + '```'  # pre-formatted, fixed-width text

    # Slack wants the body on POST to be urlencoded.
    result = salt.utils.slack.query(function='message',
                                    api_key=api_key,
                                    method='POST',
                                    header_dict={'Content-Type': 'application/x-www-form-urlencoded'},
                                    data=_urlencode(parameters))

    log.debug('Slack message post result: %s', result)
    if result:
        return True
    else:
        return False