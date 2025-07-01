def _get_data_schema(self):
        """
        Returns a dictionary of (column : type) for the data used in the
        model.
        """

        if not hasattr(self, "_data_schema"):
            response = self.__proxy__.get_data_schema()

            self._data_schema = {k : _turicreate._cython.cy_flexible_type.pytype_from_type_name(v)
                                 for k, v in response["schema"].items()}

        return self._data_schema