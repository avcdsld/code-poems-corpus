def _check_state(self):
        """Helper for :meth:`commit` et al.

        :raises: :exc:`ValueError` if the object's state is invalid for making
                 API requests.
        """
        if self._transaction_id is None:
            raise ValueError("Transaction is not begun")

        if self.committed is not None:
            raise ValueError("Transaction is already committed")

        if self._rolled_back:
            raise ValueError("Transaction is already rolled back")