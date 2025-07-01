def filter_by(self, values, column_name, exclude=False):
        """
        Filter an SFrame by values inside an iterable object. Result is an
        SFrame that only includes (or excludes) the rows that have a column
        with the given ``column_name`` which holds one of the values in the
        given ``values`` :class:`~turicreate.SArray`. If ``values`` is not an
        SArray, we attempt to convert it to one before filtering.

        Parameters
        ----------
        values : SArray | list | numpy.ndarray | pandas.Series | str
            The values to use to filter the SFrame.  The resulting SFrame will
            only include rows that have one of these values in the given
            column.

        column_name : str
            The column of the SFrame to match with the given `values`.

        exclude : bool
            If True, the result SFrame will contain all rows EXCEPT those that
            have one of ``values`` in ``column_name``.

        Returns
        -------
        out : SFrame
            The filtered SFrame.

        Examples
        --------
        >>> sf = turicreate.SFrame({'id': [1, 2, 3, 4],
        ...                      'animal_type': ['dog', 'cat', 'cow', 'horse'],
        ...                      'name': ['bob', 'jim', 'jimbob', 'bobjim']})
        >>> household_pets = ['cat', 'hamster', 'dog', 'fish', 'bird', 'snake']
        >>> sf.filter_by(household_pets, 'animal_type')
        +-------------+----+------+
        | animal_type | id | name |
        +-------------+----+------+
        |     dog     | 1  | bob  |
        |     cat     | 2  | jim  |
        +-------------+----+------+
        [2 rows x 3 columns]
        >>> sf.filter_by(household_pets, 'animal_type', exclude=True)
        +-------------+----+--------+
        | animal_type | id |  name  |
        +-------------+----+--------+
        |    horse    | 4  | bobjim |
        |     cow     | 3  | jimbob |
        +-------------+----+--------+
        [2 rows x 3 columns]
        """
        if type(column_name) is not str:
            raise TypeError("Must pass a str as column_name")

        existing_columns = self.column_names()
        if column_name not in existing_columns:
            raise KeyError("Column '" + column_name + "' not in SFrame.")

        if type(values) is not SArray:
            # If we were given a single element, try to put in list and convert
            # to SArray
            if not _is_non_string_iterable(values):
                values = [values]
            values = SArray(values)

        value_sf = SFrame()
        value_sf.add_column(values, column_name, inplace=True)

        existing_type = self.column_types()[self.column_names().index(column_name)]
        given_type = value_sf.column_types()[0]
        if given_type != existing_type:
            raise TypeError("Type of given values does not match type of column '" +
                column_name + "' in SFrame.")

        # Make sure the values list has unique values, or else join will not
        # filter.
        value_sf = value_sf.groupby(column_name, {})

        with cython_context():
            if exclude:
                id_name = "id"
                # Make sure this name is unique so we know what to remove in
                # the result
                while id_name in existing_columns:
                    id_name += "1"
                value_sf = value_sf.add_row_number(id_name)

                tmp = SFrame(_proxy=self.__proxy__.join(value_sf.__proxy__,
                                                     'left',
                                                     {column_name:column_name}))
                ret_sf = tmp[tmp[id_name] == None]
                del ret_sf[id_name]
                return ret_sf
            else:
                return SFrame(_proxy=self.__proxy__.join(value_sf.__proxy__,
                                                     'inner',
                                                     {column_name:column_name}))