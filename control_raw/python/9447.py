def sendintr(self):
        '''This sends a SIGINT to the child. It does not require
        the SIGINT to be the first character on a line. '''

        n, byte = self.ptyproc.sendintr()
        self._log_control(byte)