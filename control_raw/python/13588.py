def _list_like_func(self, func, axis, *args, **kwargs):
        """Apply list-like function across given axis.

        Args:
            func: The function to apply.
            axis: Target axis to apply the function along.

        Returns:
            A new PandasQueryCompiler.
        """
        func_prepared = self._prepare_method(
            lambda df: pandas.DataFrame(df.apply(func, axis, *args, **kwargs))
        )
        new_data = self._map_across_full_axis(axis, func_prepared)
        # When the function is list-like, the function names become the index/columns
        new_index = (
            [f if isinstance(f, string_types) else f.__name__ for f in func]
            if axis == 0
            else self.index
        )
        new_columns = (
            [f if isinstance(f, string_types) else f.__name__ for f in func]
            if axis == 1
            else self.columns
        )
        return self.__constructor__(new_data, new_index, new_columns)