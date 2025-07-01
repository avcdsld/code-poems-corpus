def _init_from_dt(self, data, nthread):
        """
        Initialize data from a datatable Frame.
        """
        ptrs = (ctypes.c_void_p * data.ncols)()
        if hasattr(data, "internal") and hasattr(data.internal, "column"):
            # datatable>0.8.0
            for icol in range(data.ncols):
                col = data.internal.column(icol)
                ptr = col.data_pointer
                ptrs[icol] = ctypes.c_void_p(ptr)
        else:
            # datatable<=0.8.0
            from datatable.internal import frame_column_data_r  # pylint: disable=no-name-in-module,import-error
            for icol in range(data.ncols):
                ptrs[icol] = frame_column_data_r(data, icol)

        # always return stypes for dt ingestion
        feature_type_strings = (ctypes.c_char_p * data.ncols)()
        for icol in range(data.ncols):
            feature_type_strings[icol] = ctypes.c_char_p(data.stypes[icol].name.encode('utf-8'))

        handle = ctypes.c_void_p()
        _check_call(_LIB.XGDMatrixCreateFromDT(
            ptrs, feature_type_strings,
            c_bst_ulong(data.shape[0]),
            c_bst_ulong(data.shape[1]),
            ctypes.byref(handle),
            nthread))
        self.handle = handle