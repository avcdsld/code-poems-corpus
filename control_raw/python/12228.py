async def close_all_connections(self) -> None:
        """Close all open connections and asynchronously wait for them to finish.

        This method is used in combination with `~.TCPServer.stop` to
        support clean shutdowns (especially for unittests). Typical
        usage would call ``stop()`` first to stop accepting new
        connections, then ``await close_all_connections()`` to wait for
        existing connections to finish.

        This method does not currently close open websocket connections.

        Note that this method is a coroutine and must be caled with ``await``.

        """
        while self._connections:
            # Peek at an arbitrary element of the set
            conn = next(iter(self._connections))
            await conn.close()