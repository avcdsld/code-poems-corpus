def _parse_block(self):
        """Parse metadata and rows from the block only once."""
        if self._iter_rows is not None:
            return

        rows = _avro_rows(self._block, self._avro_schema)
        self._num_items = self._block.avro_rows.row_count
        self._remaining = self._block.avro_rows.row_count
        self._iter_rows = iter(rows)