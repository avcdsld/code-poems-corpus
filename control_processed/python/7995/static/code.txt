def debug_str(self):
        """Get a debug string about internal execution plan.

        Returns
        -------
        debug_str : string
            Debug string of the executor.

        Examples
        --------
        >>> a = mx.sym.Variable('a')
        >>> b = mx.sym.sin(a)
        >>> c = 2 * a + b
        >>> texec = c.bind(mx.cpu(), {'a': mx.nd.array([1,2]), 'b':mx.nd.array([2,3])})
        >>> print(texec.debug_str())
        Symbol Outputs:
	            output[0]=_plus0(0)
        Variable:a
        --------------------
        Op:_mul_scalar, Name=_mulscalar0
        Inputs:
	        arg[0]=a(0) version=0
        Attrs:
	        scalar=2
        --------------------
        Op:sin, Name=sin0
        Inputs:
	        arg[0]=a(0) version=0
        --------------------
        Op:elemwise_add, Name=_plus0
        Inputs:
	        arg[0]=_mulscalar0(0)
	        arg[1]=sin0(0)
        Total 0 MB allocated
        Total 11 TempSpace resource requested
        """
        debug_str = ctypes.c_char_p()
        check_call(_LIB.MXExecutorPrint(
            self.handle, ctypes.byref(debug_str)))
        return py_str(debug_str.value)