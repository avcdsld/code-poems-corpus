def _write_items(self, row_lookup, col_lookup, item):
        """Perform remote write and replace blocks.
        """
        self.qc.write_items(row_lookup, col_lookup, item)