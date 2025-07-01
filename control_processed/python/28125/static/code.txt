def authenticate(username, password):
    '''
    Returns True if the given username and password authenticate for the
    given service.  Returns False otherwise

    ``username``: the username to authenticate

    ``password``: the password in plain text
    '''
    service = __opts__.get('auth.pam.service', 'login')

    if isinstance(username, six.text_type):
        username = username.encode(__salt_system_encoding__)
    if isinstance(password, six.text_type):
        password = password.encode(__salt_system_encoding__)
    if isinstance(service, six.text_type):
        service = service.encode(__salt_system_encoding__)

    @CONV_FUNC
    def my_conv(n_messages, messages, p_response, app_data):
        '''
        Simple conversation function that responds to any
        prompt where the echo is off with the supplied password
        '''
        # Create an array of n_messages response objects
        addr = CALLOC(n_messages, sizeof(PamResponse))
        p_response[0] = cast(addr, POINTER(PamResponse))
        for i in range(n_messages):
            if messages[i].contents.msg_style == PAM_PROMPT_ECHO_OFF:
                pw_copy = STRDUP(password)
                p_response.contents[i].resp = cast(pw_copy, c_char_p)
                p_response.contents[i].resp_retcode = 0
        return 0

    handle = PamHandle()
    conv = PamConv(my_conv, 0)
    retval = PAM_START(service, username, pointer(conv), pointer(handle))

    if retval != 0:
        # TODO: This is not an authentication error, something
        # has gone wrong starting up PAM
        PAM_END(handle, retval)
        return False

    retval = PAM_AUTHENTICATE(handle, 0)
    if retval == 0:
        PAM_ACCT_MGMT(handle, 0)
    PAM_END(handle, 0)
    return retval == 0