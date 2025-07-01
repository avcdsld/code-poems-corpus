def print_rows(self, num_rows=10, num_columns=40, max_column_width=30,
                   max_row_width=80, output_file=None):
        """
        Print the first M rows and N columns of the SFrame in human readable
        format.

        Parameters
        ----------
        num_rows : int, optional
            Number of rows to print.

        num_columns : int, optional
            Number of columns to print.

        max_column_width : int, optional
            Maximum width of a column. Columns use fewer characters if possible.

        max_row_width : int, optional
            Maximum width of a printed row. Columns beyond this width wrap to a
            new line. `max_row_width` is automatically reset to be the
            larger of itself and `max_column_width`.

        output_file: file, optional
            The stream or file that receives the output. By default the output
            goes to sys.stdout, but it can also be redirected to a file or a
            string (using an object of type StringIO).

        See Also
        --------
        head, tail
        """
        if output_file is None:
            output_file = sys.stdout

        max_row_width = max(max_row_width, max_column_width + 1)

        printed_sf = self._imagecols_to_stringcols(num_rows)
        row_of_tables = printed_sf.__get_pretty_tables__(wrap_text=False,
                                                         max_rows_to_display=num_rows,
                                                         max_columns=num_columns,
                                                         max_column_width=max_column_width,
                                                         max_row_width=max_row_width)
        footer = "[%d rows x %d columns]\n" % self.shape
        print('\n'.join([str(tb) for tb in row_of_tables]) + "\n" + footer, file=output_file)