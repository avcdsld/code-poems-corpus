def copyto(self, other):
        """Copies the value of this array to another array.

        If ``other`` is a ``NDArray`` object, then ``other.shape`` and
        ``self.shape`` should be the same. This function copies the value from
        ``self`` to ``other``.

        If ``other`` is a context, a new ``NDArray`` will be first created on
        the target context, and the value of ``self`` is copied.

        Parameters
        ----------
        other : NDArray or Context
            The destination array or context.

        Returns
        -------
        NDArray, CSRNDArray or RowSparseNDArray
            The copied array. If ``other`` is an ``NDArray``, then the return value
            and ``other`` will point to the same ``NDArray``.

        Examples
        --------
        >>> x = mx.nd.ones((2,3))
        >>> y = mx.nd.zeros((2,3), mx.gpu(0))
        >>> z = x.copyto(y)
        >>> z is y
        True
        >>> y.asnumpy()
        array([[ 1.,  1.,  1.],
               [ 1.,  1.,  1.]], dtype=float32)
        >>> y.copyto(mx.gpu(0))
        <NDArray 2x3 @gpu(0)>

        """
        if isinstance(other, NDArray):
            if other.handle is self.handle:
                warnings.warn('You are attempting to copy an array to itself', RuntimeWarning)
                return False
            return _internal._copyto(self, out=other)
        elif isinstance(other, Context):
            hret = NDArray(_new_alloc_handle(self.shape, other, True, self.dtype))
            return _internal._copyto(self, out=hret)
        else:
            raise TypeError('copyto does not support type ' + str(type(other)))