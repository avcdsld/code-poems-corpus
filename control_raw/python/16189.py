def split_datetime(self, column_name, column_name_prefix=None, limit=None, timezone=False):
        """
        Splits a datetime column of SFrame to multiple columns, with each value in a
        separate column. Returns a new SFrame with the expanded column replaced with
        a list of new columns. The expanded column must be of datetime type.

        For more details regarding name generation and
        other, refer to :py:func:`turicreate.SArray.split_datetime()`

        Parameters
        ----------
        column_name : str
            Name of the unpacked column.

        column_name_prefix : str, optional
            If provided, expanded column names would start with the given prefix.
            If not provided, the default value is the name of the expanded column.

        limit: list[str], optional
            Limits the set of datetime elements to expand.
            Possible values are 'year','month','day','hour','minute','second',
            'weekday', 'isoweekday', 'tmweekday', and 'us'.
            If not provided, only ['year','month','day','hour','minute','second']
            are expanded.

        timezone : bool, optional
            A boolean parameter that determines whether to show the timezone
            column or not. Defaults to False.

        Returns
        -------
        out : SFrame
            A new SFrame that contains rest of columns from original SFrame with
            the given column replaced with a collection of expanded columns.

        Examples
        ---------

        >>> sf
        Columns:
            id   int
            submission  datetime
        Rows: 2
        Data:
            +----+-------------------------------------------------+
            | id |               submission                        |
            +----+-------------------------------------------------+
            | 1  | datetime(2011, 1, 21, 7, 17, 21, tzinfo=GMT(+1))|
            | 2  | datetime(2011, 1, 21, 5, 43, 21, tzinfo=GMT(+1))|
            +----+-------------------------------------------------+

        >>> sf.split_datetime('submission',limit=['hour','minute'])
        Columns:
            id  int
            submission.hour int
            submission.minute int
        Rows: 2
        Data:
        +----+-----------------+-------------------+
        | id | submission.hour | submission.minute |
        +----+-----------------+-------------------+
        | 1  |        7        |        17         |
        | 2  |        5        |        43         |
        +----+-----------------+-------------------+
        """
        if column_name not in self.column_names():
            raise KeyError("column '" + column_name + "' does not exist in current SFrame")

        if column_name_prefix is None:
            column_name_prefix = column_name

        new_sf = self[column_name].split_datetime(column_name_prefix, limit, timezone)

        # construct return SFrame, check if there is conflict
        rest_columns =  [name for name in self.column_names() if name != column_name]
        new_names = new_sf.column_names()
        while set(new_names).intersection(rest_columns):
            new_names = [name + ".1" for name in new_names]
        new_sf.rename(dict(list(zip(new_sf.column_names(), new_names))), inplace=True)

        ret_sf = self.select_columns(rest_columns)
        ret_sf.add_columns(new_sf, inplace=True)
        return ret_sf