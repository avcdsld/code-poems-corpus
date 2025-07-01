def _copy_from_previous(self, cell):
        """Helper for :meth:`consume_next`."""
        previous = self._previous_cell
        if previous is not None:
            if not cell.row_key:
                cell.row_key = previous.row_key
                if not cell.family_name:
                    cell.family_name = previous.family_name
                    # NOTE: ``cell.qualifier`` **can** be empty string.
                    if cell.qualifier is None:
                        cell.qualifier = previous.qualifier