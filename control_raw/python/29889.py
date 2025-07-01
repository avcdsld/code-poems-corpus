def _quote_username(name):
    '''
    Usernames can only contain ascii chars, so make sure we return a str type
    '''
    if not isinstance(name, six.string_types):
        return str(name)  # future lint: disable=blacklisted-function
    else:
        return salt.utils.stringutils.to_str(name)