def _process_server_headers(
        self, key: Union[str, bytes], headers: httputil.HTTPHeaders
    ) -> None:
        """Process the headers sent by the server to this client connection.

        'key' is the websocket handshake challenge/response key.
        """
        assert headers["Upgrade"].lower() == "websocket"
        assert headers["Connection"].lower() == "upgrade"
        accept = self.compute_accept_value(key)
        assert headers["Sec-Websocket-Accept"] == accept

        extensions = self._parse_extensions_header(headers)
        for ext in extensions:
            if ext[0] == "permessage-deflate" and self._compression_options is not None:
                self._create_compressors("client", ext[1])
            else:
                raise ValueError("unsupported extension %r", ext)

        self.selected_subprotocol = headers.get("Sec-WebSocket-Protocol", None)