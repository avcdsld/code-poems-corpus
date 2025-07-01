def validate_enabled(enabled):
    '''
    Helper function to validate the enabled parameter. Boolean values are
    converted to "on" and "off". String values are checked to make sure they are
    either "on" or "off"/"yes" or "no". Integer ``0`` will return "off". All
    other integers will return "on"

    :param enabled: Enabled can be boolean True or False, Integers, or string
    values "on" and "off"/"yes" and "no".
    :type: str, int, bool

    :return: "on" or "off" or errors
    :rtype: str
    '''
    if isinstance(enabled, six.string_types):
        if enabled.lower() not in ['on', 'off', 'yes', 'no']:
            msg = '\nMac Power: Invalid String Value for Enabled.\n' \
                  'String values must be \'on\' or \'off\'/\'yes\' or \'no\'.\n' \
                  'Passed: {0}'.format(enabled)
            raise SaltInvocationError(msg)

        return 'on' if enabled.lower() in ['on', 'yes'] else 'off'

    return 'on' if bool(enabled) else 'off'