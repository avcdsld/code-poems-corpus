def dropna_split(self, columns=None, how='any'):
        """
        Split rows with missing values from this SFrame. This function has the
        same functionality as :py:func:`~turicreate.SFrame.dropna`, but returns a
        tuple of two SFrames.  The first item is the expected output from
        :py:func:`~turicreate.SFrame.dropna`, and the second item contains all the
        rows filtered out by the `dropna` algorithm.

        Parameters
        ----------
        columns : list or str, optional
            The columns to use when looking for missing values. By default, all
            columns are used.

        how : {'any', 'all'}, optional
            Specifies whether a row should be dropped if at least one column
            has missing values, or if all columns have missing values.  'any' is
            default.

        Returns
        -------
        out : (SFrame, SFrame)
            (SFrame with missing values removed,
             SFrame with the removed missing values)

        See Also
        --------
        dropna

        Examples
        --------
        >>> sf = turicreate.SFrame({'a': [1, None, None], 'b': ['a', 'b', None]})
        >>> good, bad = sf.dropna_split()
        >>> good
        +---+---+
        | a | b |
        +---+---+
        | 1 | a |
        +---+---+
        [1 rows x 2 columns]

        >>> bad
        +------+------+
        |  a   |  b   |
        +------+------+
        | None |  b   |
        | None | None |
        +------+------+
        [2 rows x 2 columns]
        """

        # If the user gives me an empty list (the indicator to use all columns)
        # NA values being dropped would not be the expected behavior. This
        # is a NOOP, so let's not bother the server
        if type(columns) is list and len(columns) == 0:
            return (SFrame(_proxy=self.__proxy__), SFrame())

        (columns, all_behavior) = self.__dropna_errchk(columns, how)

        sframe_tuple = self.__proxy__.drop_missing_values(columns, all_behavior, True)

        if len(sframe_tuple) != 2:
            raise RuntimeError("Did not return two SFrames!")

        with cython_context():
            return (SFrame(_proxy=sframe_tuple[0]), SFrame(_proxy=sframe_tuple[1]))