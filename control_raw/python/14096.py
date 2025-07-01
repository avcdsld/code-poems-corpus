def begin_pending_transactions(self):
        """Begin all transactions for sessions added to the pool."""
        while not self._pending_sessions.empty():
            session = self._pending_sessions.get()
            session._transaction.begin()
            super(TransactionPingingPool, self).put(session)