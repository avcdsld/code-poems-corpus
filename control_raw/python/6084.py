def mode_date(self, rows: List[Row], column: DateColumn) -> Date:
        """
        Takes a list of rows and a column and returns the most frequent value under
        that column in those rows.
        """
        most_frequent_list = self._get_most_frequent_values(rows, column)
        if not most_frequent_list:
            return Date(-1, -1, -1)
        most_frequent_value = most_frequent_list[0]
        if not isinstance(most_frequent_value, Date):
            raise ExecutionError(f"Invalid valus for mode_date: {most_frequent_value}")
        return most_frequent_value