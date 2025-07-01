def argmax(self, rows: List[Row], column: ComparableColumn) -> List[Row]:
        """
        Takes a list of rows and a column name and returns a list containing a single row (dict from
        columns to cells) that has the maximum numerical value in the given column. We return a list
        instead of a single dict to be consistent with the return type of ``select`` and
        ``all_rows``.
        """
        if not rows:
            return []
        value_row_pairs = [(row.values[column.name], row) for row in rows]
        if not value_row_pairs:
            return []
        # Returns a list containing the row with the max cell value.
        return [sorted(value_row_pairs, key=lambda x: x[0], reverse=True)[0][1]]