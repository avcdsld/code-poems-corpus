def try_read_prompt(self, timeout_multiplier):
        '''This facilitates using communication timeouts to perform
        synchronization as quickly as possible, while supporting high latency
        connections with a tunable worst case performance. Fast connections
        should be read almost immediately. Worst case performance for this
        method is timeout_multiplier * 3 seconds.
        '''

        # maximum time allowed to read the first response
        first_char_timeout = timeout_multiplier * 0.5

        # maximum time allowed between subsequent characters
        inter_char_timeout = timeout_multiplier * 0.1

        # maximum time for reading the entire prompt
        total_timeout = timeout_multiplier * 3.0

        prompt = self.string_type()
        begin = time.time()
        expired = 0.0
        timeout = first_char_timeout

        while expired < total_timeout:
            try:
                prompt += self.read_nonblocking(size=1, timeout=timeout)
                expired = time.time() - begin # updated total time expired
                timeout = inter_char_timeout
            except TIMEOUT:
                break

        return prompt