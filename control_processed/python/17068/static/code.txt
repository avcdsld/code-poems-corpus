def rolling_max(self, window_start, window_end, min_observations=None):
        """
        Calculate a new SArray of the maximum value of different subsets over
        this SArray.

        The subset that the maximum is calculated over is defined as an
        inclusive range relative to the position to each value in the SArray,
        using `window_start` and `window_end`. For a better understanding of
        this, see the examples below.

        Parameters
        ----------
        window_start : int
            The start of the subset to calculate the maximum relative to the
            current value.

        window_end : int
            The end of the subset to calculate the maximum relative to the current
            value. Must be greater than `window_start`.

        min_observations : int
            Minimum number of non-missing observations in window required to
            calculate the maximum (otherwise result is None). None signifies that
            the entire window must not include a missing value. A negative
            number throws an error.

        Returns
        -------
        out : SArray

        Examples
        --------
        >>> import pandas
        >>> sa = SArray([1,2,3,4,5])
        >>> series = pandas.Series([1,2,3,4,5])

        A rolling max with a window including the previous 2 entries including
        the current:
        >>> sa.rolling_max(-2,0)
        dtype: int
        Rows: 5
        [None, None, 3, 4, 5]

        Pandas equivalent:
        >>> pandas.rolling_max(series, 3)
        0   NaN
        1   NaN
        2     3
        3     4
        4     5
        dtype: float64

        Same rolling max operation, but 2 minimum observations:
        >>> sa.rolling_max(-2,0,min_observations=2)
        dtype: int
        Rows: 5
        [None, 2, 3, 4, 5]

        Pandas equivalent:
        >>> pandas.rolling_max(series, 3, min_periods=2)
        0    NaN
        1      2
        2      3
        3      4
        4      5
        dtype: float64

        A rolling max with a size of 3, centered around the current:
        >>> sa.rolling_max(-1,1)
        dtype: int
        Rows: 5
        [None, 3, 4, 5, None]

        Pandas equivalent:
        >>> pandas.rolling_max(series, 3, center=True)
        0   NaN
        1     3
        2     4
        3     5
        4   NaN
        dtype: float64

        A rolling max with a window including the current and the 2 entries
        following:
        >>> sa.rolling_max(0,2)
        dtype: int
        Rows: 5
        [3, 4, 5, None, None]

        A rolling max with a window including the previous 2 entries NOT
        including the current:
        >>> sa.rolling_max(-2,-1)
        dtype: int
        Rows: 5
        [None, None, 2, 3, 4]
        """
        min_observations = self.__check_min_observations(min_observations)
        agg_op = '__builtin__max__'
        return SArray(_proxy=self.__proxy__.builtin_rolling_apply(agg_op, window_start, window_end, min_observations))