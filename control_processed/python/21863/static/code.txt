def auth_gssapi_with_mic(self, username, gss_host, gss_deleg_creds):
        """
        Authenticate to the Server using GSS-API / SSPI.

        :param str username: The username to authenticate as
        :param str gss_host: The target host
        :param bool gss_deleg_creds: Delegate credentials or not
        :return: list of auth types permissible for the next stage of
                 authentication (normally empty)
        :raises: `.BadAuthenticationType` -- if gssapi-with-mic isn't
            allowed by the server (and no event was passed in)
        :raises:
            `.AuthenticationException` -- if the authentication failed (and no
            event was passed in)
        :raises: `.SSHException` -- if there was a network error
        """
        if (not self.active) or (not self.initial_kex_done):
            # we should never try to authenticate unless we're on a secure link
            raise SSHException("No existing session")
        my_event = threading.Event()
        self.auth_handler = AuthHandler(self)
        self.auth_handler.auth_gssapi_with_mic(
            username, gss_host, gss_deleg_creds, my_event
        )
        return self.auth_handler.wait_for_response(my_event)