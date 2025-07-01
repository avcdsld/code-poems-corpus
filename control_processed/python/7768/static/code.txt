def minimum(lhs, rhs):
    """Returns element-wise minimum of the input arrays with broadcasting.

    Equivalent to ``mx.nd.broadcast_minimum(lhs, rhs)``.

    .. note::

       If the corresponding dimensions of two arrays have the same size or one of them has size 1,
       then the arrays are broadcastable to a common shape.

    Parameters
    ----------
    lhs : scalar or mxnet.ndarray.array
        First array to be compared.
    rhs : scalar or mxnet.ndarray.array
         Second array to be compared. If ``lhs.shape != rhs.shape``, they must be
        broadcastable to a common shape.

    Returns
    -------
    NDArray
        The element-wise minimum of the input arrays.

    Examples
    --------
    >>> x = mx.nd.ones((2,3))
    >>> y = mx.nd.arange(2).reshape((2,1))
    >>> z = mx.nd.arange(2).reshape((1,2))
    >>> x.asnumpy()
    array([[ 1.,  1.,  1.],
           [ 1.,  1.,  1.]], dtype=float32)
    >>> y.asnumpy()
    array([[ 0.],
           [ 1.]], dtype=float32)
    >>> z.asnumpy()
    array([[ 0.,  1.]], dtype=float32)
    >>> mx.nd.minimum(x, 2).asnumpy()
    array([[ 1.,  1.,  1.],
           [ 1.,  1.,  1.]], dtype=float32)
    >>> mx.nd.minimum(x, y).asnumpy()
    array([[ 0.,  0.,  0.],
           [ 1.,  1.,  1.]], dtype=float32)
    >>> mx.nd.minimum(z, y).asnumpy()
    array([[ 0.,  0.],
           [ 0.,  1.]], dtype=float32)
    """
    # pylint: disable= no-member, protected-access
    return _ufunc_helper(
        lhs,
        rhs,
        op.broadcast_minimum,
        lambda x, y: x if x < y else y,
        _internal._minimum_scalar,
        None)