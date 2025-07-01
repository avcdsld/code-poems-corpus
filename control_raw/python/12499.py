def put_nowait(self, item: _T) -> None:
        """Put an item into the queue without blocking.

        If no free slot is immediately available, raise `QueueFull`.
        """
        self._consume_expired()
        if self._getters:
            assert self.empty(), "queue non-empty, why are getters waiting?"
            getter = self._getters.popleft()
            self.__put_internal(item)
            future_set_result_unless_cancelled(getter, self._get())
        elif self.full():
            raise QueueFull
        else:
            self.__put_internal(item)