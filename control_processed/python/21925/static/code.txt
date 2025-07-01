def _auth(
        self,
        username,
        password,
        pkey,
        key_filenames,
        allow_agent,
        look_for_keys,
        gss_auth,
        gss_kex,
        gss_deleg_creds,
        gss_host,
        passphrase,
    ):
        """
        Try, in order:

            - The key(s) passed in, if one was passed in.
            - Any key we can find through an SSH agent (if allowed).
            - Any "id_rsa", "id_dsa" or "id_ecdsa" key discoverable in ~/.ssh/
              (if allowed).
            - Plain username/password auth, if a password was given.

        (The password might be needed to unlock a private key [if 'passphrase'
        isn't also given], or for two-factor authentication [for which it is
        required].)
        """
        saved_exception = None
        two_factor = False
        allowed_types = set()
        two_factor_types = {"keyboard-interactive", "password"}
        if passphrase is None and password is not None:
            passphrase = password

        # If GSS-API support and GSS-PI Key Exchange was performed, we attempt
        # authentication with gssapi-keyex.
        if gss_kex and self._transport.gss_kex_used:
            try:
                self._transport.auth_gssapi_keyex(username)
                return
            except Exception as e:
                saved_exception = e

        # Try GSS-API authentication (gssapi-with-mic) only if GSS-API Key
        # Exchange is not performed, because if we use GSS-API for the key
        # exchange, there is already a fully established GSS-API context, so
        # why should we do that again?
        if gss_auth:
            try:
                return self._transport.auth_gssapi_with_mic(
                    username, gss_host, gss_deleg_creds
                )
            except Exception as e:
                saved_exception = e

        if pkey is not None:
            try:
                self._log(
                    DEBUG,
                    "Trying SSH key {}".format(
                        hexlify(pkey.get_fingerprint())
                    ),
                )
                allowed_types = set(
                    self._transport.auth_publickey(username, pkey)
                )
                two_factor = allowed_types & two_factor_types
                if not two_factor:
                    return
            except SSHException as e:
                saved_exception = e

        if not two_factor:
            for key_filename in key_filenames:
                for pkey_class in (RSAKey, DSSKey, ECDSAKey, Ed25519Key):
                    try:
                        key = self._key_from_filepath(
                            key_filename, pkey_class, passphrase
                        )
                        allowed_types = set(
                            self._transport.auth_publickey(username, key)
                        )
                        two_factor = allowed_types & two_factor_types
                        if not two_factor:
                            return
                        break
                    except SSHException as e:
                        saved_exception = e

        if not two_factor and allow_agent:
            if self._agent is None:
                self._agent = Agent()

            for key in self._agent.get_keys():
                try:
                    id_ = hexlify(key.get_fingerprint())
                    self._log(DEBUG, "Trying SSH agent key {}".format(id_))
                    # for 2-factor auth a successfully auth'd key password
                    # will return an allowed 2fac auth method
                    allowed_types = set(
                        self._transport.auth_publickey(username, key)
                    )
                    two_factor = allowed_types & two_factor_types
                    if not two_factor:
                        return
                    break
                except SSHException as e:
                    saved_exception = e

        if not two_factor:
            keyfiles = []

            for keytype, name in [
                (RSAKey, "rsa"),
                (DSSKey, "dsa"),
                (ECDSAKey, "ecdsa"),
                (Ed25519Key, "ed25519"),
            ]:
                # ~/ssh/ is for windows
                for directory in [".ssh", "ssh"]:
                    full_path = os.path.expanduser(
                        "~/{}/id_{}".format(directory, name)
                    )
                    if os.path.isfile(full_path):
                        # TODO: only do this append if below did not run
                        keyfiles.append((keytype, full_path))
                        if os.path.isfile(full_path + "-cert.pub"):
                            keyfiles.append((keytype, full_path + "-cert.pub"))

            if not look_for_keys:
                keyfiles = []

            for pkey_class, filename in keyfiles:
                try:
                    key = self._key_from_filepath(
                        filename, pkey_class, passphrase
                    )
                    # for 2-factor auth a successfully auth'd key will result
                    # in ['password']
                    allowed_types = set(
                        self._transport.auth_publickey(username, key)
                    )
                    two_factor = allowed_types & two_factor_types
                    if not two_factor:
                        return
                    break
                except (SSHException, IOError) as e:
                    saved_exception = e

        if password is not None:
            try:
                self._transport.auth_password(username, password)
                return
            except SSHException as e:
                saved_exception = e
        elif two_factor:
            try:
                self._transport.auth_interactive_dumb(username)
                return
            except SSHException as e:
                saved_exception = e

        # if we got an auth-failed exception earlier, re-raise it
        if saved_exception is not None:
            raise saved_exception
        raise SSHException("No authentication methods available")