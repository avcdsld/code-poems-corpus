def add_buffer(self, buf_header, buf_payload):
        ''' Associate a buffer header and payload with this message.

        Args:
            buf_header (``JSON``) : a buffer header
            buf_payload (``JSON`` or bytes) : a buffer payload

        Returns:
            None

        Raises:
            MessageError

        '''
        if 'num_buffers' in self._header:
            self._header['num_buffers'] += 1
        else:
            self._header['num_buffers'] = 1

        self._header_json = None

        self._buffers.append((buf_header, buf_payload))