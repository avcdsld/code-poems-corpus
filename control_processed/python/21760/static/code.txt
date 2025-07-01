def start_kex(self):
        """
        Start the GSS-API / SSPI Authenticated Diffie-Hellman Key Exchange.
        """
        self._generate_x()
        if self.transport.server_mode:
            # compute f = g^x mod p, but don't send it yet
            self.f = pow(self.G, self.x, self.P)
            self.transport._expect_packet(MSG_KEXGSS_INIT)
            return
        # compute e = g^x mod p (where g=2), and send it
        self.e = pow(self.G, self.x, self.P)
        # Initialize GSS-API Key Exchange
        self.gss_host = self.transport.gss_host
        m = Message()
        m.add_byte(c_MSG_KEXGSS_INIT)
        m.add_string(self.kexgss.ssh_init_sec_context(target=self.gss_host))
        m.add_mpint(self.e)
        self.transport._send_message(m)
        self.transport._expect_packet(
            MSG_KEXGSS_HOSTKEY,
            MSG_KEXGSS_CONTINUE,
            MSG_KEXGSS_COMPLETE,
            MSG_KEXGSS_ERROR,
        )