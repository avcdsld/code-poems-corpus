def run_in_transaction(self, func, *args, **kw):
        """Perform a unit of work in a transaction, retrying on abort.

        :type func: callable
        :param func: takes a required positional argument, the transaction,
                     and additional positional / keyword arguments as supplied
                     by the caller.

        :type args: tuple
        :param args: additional positional arguments to be passed to ``func``.

        :type kw: dict
        :param kw: optional keyword arguments to be passed to ``func``.
                   If passed, "timeout_secs" will be removed and used to
                   override the default timeout.

        :rtype: :class:`datetime.datetime`
        :returns: timestamp of committed transaction
        """
        # Sanity check: Is there a transaction already running?
        # If there is, then raise a red flag. Otherwise, mark that this one
        # is running.
        if getattr(self._local, "transaction_running", False):
            raise RuntimeError("Spanner does not support nested transactions.")
        self._local.transaction_running = True

        # Check out a session and run the function in a transaction; once
        # done, flip the sanity check bit back.
        try:
            with SessionCheckout(self._pool) as session:
                return session.run_in_transaction(func, *args, **kw)
        finally:
            self._local.transaction_running = False