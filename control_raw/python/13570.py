def eval(self, expr, **kwargs):
        """Returns a new QueryCompiler with expr evaluated on columns.

        Args:
            expr: The string expression to evaluate.

        Returns:
            A new QueryCompiler with new columns after applying expr.
        """
        columns = self.index if self._is_transposed else self.columns
        index = self.columns if self._is_transposed else self.index

        # Make a copy of columns and eval on the copy to determine if result type is
        # series or not
        columns_copy = pandas.DataFrame(columns=self.columns)
        columns_copy = columns_copy.eval(expr, inplace=False, **kwargs)
        expect_series = isinstance(columns_copy, pandas.Series)

        def eval_builder(df, **kwargs):
            # pop the `axis` parameter because it was needed to build the mapreduce
            # function but it is not a parameter used by `eval`.
            kwargs.pop("axis", None)
            df.columns = columns
            result = df.eval(expr, inplace=False, **kwargs)
            return result

        func = self._build_mapreduce_func(eval_builder, axis=1, **kwargs)
        new_data = self._map_across_full_axis(1, func)

        if expect_series:
            new_columns = [columns_copy.name]
            new_index = index
        else:
            new_columns = columns_copy.columns
            new_index = self.index
        return self.__constructor__(new_data, new_index, new_columns)