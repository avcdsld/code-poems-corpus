def row(self, row_key, filter_=None, append=False):
        """Factory to create a row associated with this table.

        For example:

        .. literalinclude:: snippets_table.py
            :start-after: [START bigtable_table_row]
            :end-before: [END bigtable_table_row]

        .. warning::

           At most one of ``filter_`` and ``append`` can be used in a
           :class:`~google.cloud.bigtable.row.Row`.

        :type row_key: bytes
        :param row_key: The key for the row being created.

        :type filter_: :class:`.RowFilter`
        :param filter_: (Optional) Filter to be used for conditional mutations.
                        See :class:`.ConditionalRow` for more details.

        :type append: bool
        :param append: (Optional) Flag to determine if the row should be used
                       for append mutations.

        :rtype: :class:`~google.cloud.bigtable.row.Row`
        :returns: A row owned by this table.
        :raises: :class:`ValueError <exceptions.ValueError>` if both
                 ``filter_`` and ``append`` are used.
        """
        if append and filter_ is not None:
            raise ValueError("At most one of filter_ and append can be set")
        if append:
            return AppendRow(row_key, self)
        elif filter_ is not None:
            return ConditionalRow(row_key, self, filter_=filter_)
        else:
            return DirectRow(row_key, self)