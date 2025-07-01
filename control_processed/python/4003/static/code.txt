def _init_from_csc(self, csc):
        """
        Initialize data from a CSC matrix.
        """
        if len(csc.indices) != len(csc.data):
            raise ValueError('length mismatch: {} vs {}'.format(len(csc.indices), len(csc.data)))
        handle = ctypes.c_void_p()
        _check_call(_LIB.XGDMatrixCreateFromCSCEx(c_array(ctypes.c_size_t, csc.indptr),
                                                  c_array(ctypes.c_uint, csc.indices),
                                                  c_array(ctypes.c_float, csc.data),
                                                  ctypes.c_size_t(len(csc.indptr)),
                                                  ctypes.c_size_t(len(csc.data)),
                                                  ctypes.c_size_t(csc.shape[0]),
                                                  ctypes.byref(handle)))
        self.handle = handle