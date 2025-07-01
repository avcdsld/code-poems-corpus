def _dt_array_cmp(cls, op):
    """
    Wrap comparison operations to convert datetime-like to datetime64
    """
    opname = '__{name}__'.format(name=op.__name__)
    nat_result = opname == '__ne__'

    def wrapper(self, other):
        if isinstance(other, (ABCDataFrame, ABCSeries, ABCIndexClass)):
            return NotImplemented

        other = lib.item_from_zerodim(other)

        if isinstance(other, (datetime, np.datetime64, str)):
            if isinstance(other, (datetime, np.datetime64)):
                # GH#18435 strings get a pass from tzawareness compat
                self._assert_tzawareness_compat(other)

            try:
                other = _to_M8(other, tz=self.tz)
            except ValueError:
                # string that cannot be parsed to Timestamp
                return ops.invalid_comparison(self, other, op)

            result = op(self.asi8, other.view('i8'))
            if isna(other):
                result.fill(nat_result)
        elif lib.is_scalar(other) or np.ndim(other) == 0:
            return ops.invalid_comparison(self, other, op)
        elif len(other) != len(self):
            raise ValueError("Lengths must match")
        else:
            if isinstance(other, list):
                try:
                    other = type(self)._from_sequence(other)
                except ValueError:
                    other = np.array(other, dtype=np.object_)
            elif not isinstance(other, (np.ndarray, ABCIndexClass, ABCSeries,
                                        DatetimeArray)):
                # Following Timestamp convention, __eq__ is all-False
                # and __ne__ is all True, others raise TypeError.
                return ops.invalid_comparison(self, other, op)

            if is_object_dtype(other):
                # We have to use _comp_method_OBJECT_ARRAY instead of numpy
                #  comparison otherwise it would fail to raise when
                #  comparing tz-aware and tz-naive
                with np.errstate(all='ignore'):
                    result = ops._comp_method_OBJECT_ARRAY(op,
                                                           self.astype(object),
                                                           other)
                o_mask = isna(other)
            elif not (is_datetime64_dtype(other) or
                      is_datetime64tz_dtype(other)):
                # e.g. is_timedelta64_dtype(other)
                return ops.invalid_comparison(self, other, op)
            else:
                self._assert_tzawareness_compat(other)
                if isinstance(other, (ABCIndexClass, ABCSeries)):
                    other = other.array

                if (is_datetime64_dtype(other) and
                        not is_datetime64_ns_dtype(other) or
                        not hasattr(other, 'asi8')):
                    # e.g. other.dtype == 'datetime64[s]'
                    # or an object-dtype ndarray
                    other = type(self)._from_sequence(other)

                result = op(self.view('i8'), other.view('i8'))
                o_mask = other._isnan

            result = com.values_from_object(result)

            if o_mask.any():
                result[o_mask] = nat_result

        if self._hasnans:
            result[self._isnan] = nat_result

        return result

    return compat.set_function_name(wrapper, opname, cls)