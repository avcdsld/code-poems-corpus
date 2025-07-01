def set_event_handler(self, event_handler):
        '''
        Invoke the event_handler callback each time an event arrives.
        '''
        assert not self._run_io_loop_sync

        if not self.cpub:
            self.connect_pub()

        self.subscriber.callbacks.add(event_handler)
        if not self.subscriber.reading:
            # This will handle reconnects
            return self.subscriber.read_async()