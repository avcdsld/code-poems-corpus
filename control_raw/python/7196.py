def attr(self, key):
        """Returns the attribute string for corresponding input key from the symbol.

        This function only works for non-grouped symbols.

        Example
        -------
        >>> data = mx.sym.Variable('data', attr={'mood': 'angry'})
        >>> data.attr('mood')
        'angry'

        Parameters
        ----------
        key : str
            The key corresponding to the desired attribute.

        Returns
        -------
        value : str
            The desired attribute value, returns ``None`` if the attribute does not exist.
        """
        ret = ctypes.c_char_p()
        success = ctypes.c_int()
        check_call(_LIB.MXSymbolGetAttr(
            self.handle, c_str(key), ctypes.byref(ret), ctypes.byref(success)))
        if success.value != 0:
            return py_str(ret.value)
        else:
            return None