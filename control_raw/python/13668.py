def _handle_enlargement(self, row_loc, col_loc):
        """Handle Enlargement (if there is one).

        Returns:
            None
        """
        if _is_enlargement(row_loc, self.qc.index) or _is_enlargement(
            col_loc, self.qc.columns
        ):
            _warn_enlargement()
            self.qc.enlarge_partitions(
                new_row_labels=self._compute_enlarge_labels(row_loc, self.qc.index),
                new_col_labels=self._compute_enlarge_labels(col_loc, self.qc.columns),
            )