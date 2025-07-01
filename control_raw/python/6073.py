def select_string(self, rows: List[Row], column: StringColumn) -> List[str]:
        """
        Select function takes a list of rows and a column name and returns a list of strings as
        in cells.
        """
        return [str(row.values[column.name]) for row in rows if row.values[column.name] is not None]