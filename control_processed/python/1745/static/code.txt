def hide_columns(self, subset):
        """
        Hide columns from rendering.

        .. versionadded:: 0.23.0

        Parameters
        ----------
        subset : IndexSlice
            An argument to ``DataFrame.loc`` that identifies which columns
            are hidden.

        Returns
        -------
        self : Styler
        """
        subset = _non_reducing_slice(subset)
        hidden_df = self.data.loc[subset]
        self.hidden_columns = self.columns.get_indexer_for(hidden_df.columns)
        return self