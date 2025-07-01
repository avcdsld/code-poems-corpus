def _arith_method_SPARSE_ARRAY(cls, op, special):
    """
    Wrapper function for Series arithmetic operations, to avoid
    code duplication.
    """
    op_name = _get_op_name(op, special)

    def wrapper(self, other):
        from pandas.core.arrays.sparse.array import (
            SparseArray, _sparse_array_op, _wrap_result, _get_fill)
        if isinstance(other, np.ndarray):
            if len(self) != len(other):
                raise AssertionError("length mismatch: {self} vs. {other}"
                                     .format(self=len(self), other=len(other)))
            if not isinstance(other, SparseArray):
                dtype = getattr(other, 'dtype', None)
                other = SparseArray(other, fill_value=self.fill_value,
                                    dtype=dtype)
            return _sparse_array_op(self, other, op, op_name)
        elif is_scalar(other):
            with np.errstate(all='ignore'):
                fill = op(_get_fill(self), np.asarray(other))
                result = op(self.sp_values, other)

            return _wrap_result(op_name, result, self.sp_index, fill)
        else:  # pragma: no cover
            raise TypeError('operation with {other} not supported'
                            .format(other=type(other)))

    wrapper.__name__ = op_name
    return wrapper