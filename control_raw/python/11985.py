async def poll_event(self):
        """Polls for a DISPATCH event and handles the general gateway loop.

        Raises
        ------
        ConnectionClosed
            The websocket connection was terminated for unhandled reasons.
        """
        try:
            msg = await self.recv()
            await self.received_message(msg)
        except websockets.exceptions.ConnectionClosed as exc:
            if self._can_handle_close(exc.code):
                log.info('Websocket closed with %s (%s), attempting a reconnect.', exc.code, exc.reason)
                raise ResumeWebSocket(self.shard_id) from exc
            else:
                log.info('Websocket closed with %s (%s), cannot reconnect.', exc.code, exc.reason)
                raise ConnectionClosed(exc, shard_id=self.shard_id) from exc