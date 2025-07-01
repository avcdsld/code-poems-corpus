def mutations_batcher(self, flush_count=FLUSH_COUNT, max_row_bytes=MAX_ROW_BYTES):
        """Factory to create a mutation batcher associated with this instance.

        For example:

        .. literalinclude:: snippets_table.py
            :start-after: [START bigtable_mutations_batcher]
            :end-before: [END bigtable_mutations_batcher]

        :type table: class
        :param table: class:`~google.cloud.bigtable.table.Table`.

        :type flush_count: int
        :param flush_count: (Optional) Maximum number of rows per batch. If it
                reaches the max number of rows it calls finish_batch() to
                mutate the current row batch. Default is FLUSH_COUNT (1000
                rows).

        :type max_row_bytes: int
        :param max_row_bytes: (Optional) Max number of row mutations size to
                flush. If it reaches the max number of row mutations size it
                calls finish_batch() to mutate the current row batch.
                Default is MAX_ROW_BYTES (5 MB).
        """
        return MutationsBatcher(self, flush_count, max_row_bytes)