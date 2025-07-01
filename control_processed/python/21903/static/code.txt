def start_handshake(self, timeout):
        """
        Tells `Packetizer` that the handshake process started.
        Starts a book keeping timer that can signal a timeout in the
        handshake process.

        :param float timeout: amount of seconds to wait before timing out
        """
        if not self.__timer:
            self.__timer = threading.Timer(float(timeout), self.read_timer)
            self.__timer.start()