def _validate_input_column(self, column):
        """Make sure a passed column is our column.
        """
        if column != self.column and column.unspecialize() != self.column:
            raise ValueError("Can't load unknown column %s" % column)