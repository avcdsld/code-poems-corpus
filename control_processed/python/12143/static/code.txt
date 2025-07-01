async def stream(
        self, version="1.1", keep_alive=False, keep_alive_timeout=None
    ):
        """Streams headers, runs the `streaming_fn` callback that writes
        content to the response body, then finalizes the response body.
        """
        headers = self.get_headers(
            version,
            keep_alive=keep_alive,
            keep_alive_timeout=keep_alive_timeout,
        )
        self.protocol.push_data(headers)
        await self.protocol.drain()
        await self.streaming_fn(self)
        self.protocol.push_data(b"0\r\n\r\n")