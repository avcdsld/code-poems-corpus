def _inter_df_op_handler(self, func, other, **kwargs):
        """Helper method for inter-manager and scalar operations.

        Args:
            func: The function to use on the Manager/scalar.
            other: The other Manager/scalar.

        Returns:
            New DataManager with new data and index.
        """
        axis = kwargs.get("axis", 0)
        axis = pandas.DataFrame()._get_axis_number(axis) if axis is not None else 0
        if isinstance(other, type(self)):
            return self._inter_manager_operations(
                other, "outer", lambda x, y: func(x, y, **kwargs)
            )
        else:
            return self._scalar_operations(
                axis, other, lambda df: func(df, other, **kwargs)
            )