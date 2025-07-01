def decode(self, input, final=False):
        """Decode one chunk of the input.

        :param input: A byte string.
        :param final:
            Indicate that no more input is available.
            Must be :obj:`True` if this is the last call.
        :returns: An Unicode string.

        """
        decoder = self._decoder
        if decoder is not None:
            return decoder(input, final)

        input = self._buffer + input
        encoding, input = _detect_bom(input)
        if encoding is None:
            if len(input) < 3 and not final:  # Not enough data yet.
                self._buffer = input
                return ''
            else:  # No BOM
                encoding = self._fallback_encoding
        decoder = encoding.codec_info.incrementaldecoder(self._errors).decode
        self._decoder = decoder
        self.encoding = encoding
        return decoder(input, final)