def modify_ack_deadline(self, seconds):
        """Resets the deadline for acknowledgement.

        New deadline will be the given value of seconds from now.

        The default implementation handles this for you; you should not need
        to manually deal with setting ack deadlines. The exception case is
        if you are implementing your own custom subclass of
        :class:`~.pubsub_v1.subcriber._consumer.Consumer`.

        Args:
            seconds (int): The number of seconds to set the lease deadline
                to. This should be between 0 and 600. Due to network latency,
                values below 10 are advised against.
        """
        self._request_queue.put(
            requests.ModAckRequest(ack_id=self._ack_id, seconds=seconds)
        )