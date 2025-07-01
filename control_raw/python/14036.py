def dispatch_callback(self, items):
        """Map the callback request to the appropriate gRPC request.

        Args:
            action (str): The method to be invoked.
            kwargs (Dict[str, Any]): The keyword arguments for the method
                specified by ``action``.

        Raises:
            ValueError: If ``action`` isn't one of the expected actions
                "ack", "drop", "lease", "modify_ack_deadline" or "nack".
        """
        if not self._manager.is_active:
            return

        batched_commands = collections.defaultdict(list)

        for item in items:
            batched_commands[item.__class__].append(item)

        _LOGGER.debug("Handling %d batched requests", len(items))

        if batched_commands[requests.LeaseRequest]:
            self.lease(batched_commands.pop(requests.LeaseRequest))
        if batched_commands[requests.ModAckRequest]:
            self.modify_ack_deadline(batched_commands.pop(requests.ModAckRequest))
        # Note: Drop and ack *must* be after lease. It's possible to get both
        # the lease the and ack/drop request in the same batch.
        if batched_commands[requests.AckRequest]:
            self.ack(batched_commands.pop(requests.AckRequest))
        if batched_commands[requests.NackRequest]:
            self.nack(batched_commands.pop(requests.NackRequest))
        if batched_commands[requests.DropRequest]:
            self.drop(batched_commands.pop(requests.DropRequest))