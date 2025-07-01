def get_adjustments(self,
                        zero_qtr_data,
                        requested_qtr_data,
                        last_per_qtr,
                        dates,
                        assets,
                        columns,
                        **kwargs):
        """
        Creates an AdjustedArray from the given estimates data for the given
        dates.

        Parameters
        ----------
        zero_qtr_data : pd.DataFrame
            The 'time zero' data for each calendar date per sid.
        requested_qtr_data : pd.DataFrame
            The requested quarter data for each calendar date per sid.
        last_per_qtr : pd.DataFrame
            A DataFrame with a column MultiIndex of [self.estimates.columns,
            normalized_quarters, sid] that allows easily getting the timeline
            of estimates for a particular sid for a particular quarter.
        dates : pd.DatetimeIndex
            The calendar dates for which estimates data is requested.
        assets : pd.Int64Index
            An index of all the assets from the raw data.
        columns : list of BoundColumn
            The columns for which adjustments need to be calculated.
        kwargs :
            Additional keyword arguments that should be forwarded to
            `get_adjustments_for_sid` and to be used in computing adjustments
            for each sid.

        Returns
        -------
        col_to_all_adjustments : dict[int -> AdjustedArray]
            A dictionary of all adjustments that should be applied.
        """

        zero_qtr_data.sort_index(inplace=True)
        # Here we want to get the LAST record from each group of records
        # corresponding to a single quarter. This is to ensure that we select
        # the most up-to-date event date in case the event date changes.
        quarter_shifts = zero_qtr_data.groupby(
            level=[SID_FIELD_NAME, NORMALIZED_QUARTERS]
        ).nth(-1)

        col_to_all_adjustments = {}
        sid_to_idx = dict(zip(assets, range(len(assets))))
        quarter_shifts.groupby(level=SID_FIELD_NAME).apply(
            self.get_adjustments_for_sid,
            dates,
            requested_qtr_data,
            last_per_qtr,
            sid_to_idx,
            columns,
            col_to_all_adjustments,
            **kwargs
        )
        return col_to_all_adjustments