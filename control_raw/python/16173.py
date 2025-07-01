def export_json(self,
                    filename,
                    orient='records'):
        """
        Writes an SFrame to a JSON file.

        Parameters
        ----------
        filename : string
            The location to save the JSON file.

        orient : string, optional. Either "records" or "lines"
            If orient="records" the file is saved as a single JSON array.
            If orient="lines", the file is saves as a JSON value per line.

        Examples
        --------
        The orient parameter describes the expected input format of the JSON
        file.

        If orient="records", the output will be a single JSON Array where
        each array element is a dictionary describing the row.

        >>> g
        Columns:
                a	int
                b	int
        Rows: 3
        Data:
        +---+---+
        | a | b |
        +---+---+
        | 1 | 1 |
        | 2 | 2 |
        | 3 | 3 |
        +---+---+
        >>> g.export('output.json', orient='records')
        >>> !cat output.json
        [
        {'a':1,'b':1},
        {'a':2,'b':2},
        {'a':3,'b':3},
        ]

        If orient="rows", each row will be emitted as a JSON dictionary to
        each file line.

        >>> g
        Columns:
                a	int
                b	int
        Rows: 3
        Data:
        +---+---+
        | a | b |
        +---+---+
        | 1 | 1 |
        | 2 | 2 |
        | 3 | 3 |
        +---+---+
        >>> g.export('output.json', orient='rows')
        >>> !cat output.json
        {'a':1,'b':1}
        {'a':2,'b':2}
        {'a':3,'b':3}
        """
        if orient == "records":
            self.pack_columns(dtype=dict).export_csv(
                    filename, file_header='[', file_footer=']',
                    header=False, double_quote=False,
                    quote_level=csv.QUOTE_NONE,
                    line_prefix=',',
                    _no_prefix_on_first_value=True)
        elif orient == "lines":
            self.pack_columns(dtype=dict).export_csv(
                    filename, header=False, double_quote=False, quote_level=csv.QUOTE_NONE)
        else:
            raise ValueError("Invalid value for orient parameter (" + str(orient) + ")")