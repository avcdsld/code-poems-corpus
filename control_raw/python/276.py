def fillna(self, value, subset=None):
        """Replace null values, alias for ``na.fill()``.
        :func:`DataFrame.fillna` and :func:`DataFrameNaFunctions.fill` are aliases of each other.

        :param value: int, long, float, string, bool or dict.
            Value to replace null values with.
            If the value is a dict, then `subset` is ignored and `value` must be a mapping
            from column name (string) to replacement value. The replacement value must be
            an int, long, float, boolean, or string.
        :param subset: optional list of column names to consider.
            Columns specified in subset that do not have matching data type are ignored.
            For example, if `value` is a string, and subset contains a non-string column,
            then the non-string column is simply ignored.

        >>> df4.na.fill(50).show()
        +---+------+-----+
        |age|height| name|
        +---+------+-----+
        | 10|    80|Alice|
        |  5|    50|  Bob|
        | 50|    50|  Tom|
        | 50|    50| null|
        +---+------+-----+

        >>> df5.na.fill(False).show()
        +----+-------+-----+
        | age|   name|  spy|
        +----+-------+-----+
        |  10|  Alice|false|
        |   5|    Bob|false|
        |null|Mallory| true|
        +----+-------+-----+

        >>> df4.na.fill({'age': 50, 'name': 'unknown'}).show()
        +---+------+-------+
        |age|height|   name|
        +---+------+-------+
        | 10|    80|  Alice|
        |  5|  null|    Bob|
        | 50|  null|    Tom|
        | 50|  null|unknown|
        +---+------+-------+
        """
        if not isinstance(value, (float, int, long, basestring, bool, dict)):
            raise ValueError("value should be a float, int, long, string, bool or dict")

        # Note that bool validates isinstance(int), but we don't want to
        # convert bools to floats

        if not isinstance(value, bool) and isinstance(value, (int, long)):
            value = float(value)

        if isinstance(value, dict):
            return DataFrame(self._jdf.na().fill(value), self.sql_ctx)
        elif subset is None:
            return DataFrame(self._jdf.na().fill(value), self.sql_ctx)
        else:
            if isinstance(subset, basestring):
                subset = [subset]
            elif not isinstance(subset, (list, tuple)):
                raise ValueError("subset should be a list or tuple of column names")

            return DataFrame(self._jdf.na().fill(value, self._jseq(subset)), self.sql_ctx)