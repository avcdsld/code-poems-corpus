def pull(self, key, out=None, priority=0, ignore_sparse=True):
        """ Pulls a single value or a sequence of values from the store.

        This function returns immediately after adding an operator to the engine.
        Subsequent attempts to read from the `out` variable will be blocked until the
        pull operation completes.

        `pull` is executed asynchronously after all previous `pull` calls and only
        the last `push` call for the same input key(s) are finished.

        The returned values are guaranteed to be the latest values in the store.

        pull with `RowSparseNDArray` is not supported for dist kvstore.
        Please use ``row_sparse_pull`` instead.

        Parameters
        ----------
        key : str, int, or sequence of str or int
            Keys.

        out: NDArray or list of NDArray or list of list of NDArray
            Values corresponding to the keys.

        priority : int, optional
            The priority of the pull operation.
            Higher priority pull operations are likely to be executed before
            other pull actions.

        ignore_sparse: bool, optional, default True
            Whether to ignore sparse arrays in the request.

        Examples
        --------
        >>> # pull a single key-value pair
        >>> a = mx.nd.zeros(shape)
        >>> kv.pull('3', out=a)
        >>> print a.asnumpy()
        [[ 2.  2.  2.]
        [ 2.  2.  2.]]

        >>> # pull into multiple devices
        >>> b = [mx.nd.ones(shape, gpu) for gpu in gpus]
        >>> kv.pull('3', out=b)
        >>> print b[1].asnumpy()
        [[ 2.  2.  2.]
        [ 2.  2.  2.]]

        >>> # pull a list of key-value pairs.
        >>> # On single device
        >>> keys = ['5', '7', '9']
        >>> b = [mx.nd.zeros(shape)]*len(keys)
        >>> kv.pull(keys, out=b)
        >>> print b[1].asnumpy()
        [[ 2.  2.  2.]
        [ 2.  2.  2.]]
        >>> # On multiple devices
        >>> keys = ['6', '8', '10']
        >>> b = [[mx.nd.ones(shape, gpu) for gpu in gpus]] * len(keys)
        >>> kv.pull(keys, out=b)
        >>> print b[1][1].asnumpy()
        [[ 2.  2.  2.]
        [ 2.  2.  2.]]
        """
        assert(out is not None)
        ckeys, cvals, use_str_keys = _ctype_key_value(key, out)
        if use_str_keys:
            check_call(_LIB.MXKVStorePullWithSparseEx(self.handle, mx_uint(len(ckeys)), ckeys,
                                                      cvals, ctypes.c_int(priority),
                                                      ctypes.c_bool(ignore_sparse)))
        else:
            check_call(_LIB.MXKVStorePullWithSparse(self.handle, mx_uint(len(ckeys)), ckeys,
                                                    cvals, ctypes.c_int(priority),
                                                    ctypes.c_bool(ignore_sparse)))