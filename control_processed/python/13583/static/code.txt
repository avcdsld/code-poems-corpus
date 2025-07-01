def drop(self, index=None, columns=None):
        """Remove row data for target index and columns.

        Args:
            index: Target index to drop.
            columns: Target columns to drop.

        Returns:
            A new QueryCompiler.
        """
        if self._is_transposed:
            return self.transpose().drop(index=columns, columns=index).transpose()
        if index is None:
            new_data = self.data
            new_index = self.index
        else:

            def delitem(df, internal_indices=[]):
                return df.drop(index=df.index[internal_indices])

            numeric_indices = list(self.index.get_indexer_for(index))
            new_data = self.data.apply_func_to_select_indices(
                1, delitem, numeric_indices, keep_remaining=True
            )
            # We can't use self.index.drop with duplicate keys because in Pandas
            # it throws an error.
            new_index = self.index[~self.index.isin(index)]
        if columns is None:
            new_columns = self.columns
            new_dtypes = self.dtypes
        else:

            def delitem(df, internal_indices=[]):
                return df.drop(columns=df.columns[internal_indices])

            numeric_indices = list(self.columns.get_indexer_for(columns))
            new_data = new_data.apply_func_to_select_indices(
                0, delitem, numeric_indices, keep_remaining=True
            )

            new_columns = self.columns[~self.columns.isin(columns)]
            new_dtypes = self.dtypes.drop(columns)
        return self.__constructor__(new_data, new_index, new_columns, new_dtypes)