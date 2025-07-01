def gamma(alpha=1, beta=1, shape=_Null, dtype=_Null, ctx=None, out=None, **kwargs):
    """Draw random samples from a gamma distribution.

    Samples are distributed according to a gamma distribution parametrized
    by *alpha* (shape) and *beta* (scale).

    Parameters
    ----------
    alpha : float or NDArray, optional
        The shape of the gamma distribution. Should be greater than zero.
    beta : float or NDArray, optional
        The scale of the gamma distribution. Should be greater than zero.
        Default is equal to 1.
    shape : int or tuple of ints, optional
        The number of samples to draw. If shape is, e.g., `(m, n)` and `alpha` and
        `beta` are scalars, output shape will be `(m, n)`. If `alpha` and `beta`
        are NDArrays with shape, e.g., `(x, y)`, then output will have shape
        `(x, y, m, n)`, where `m*n` samples are drawn for each `[alpha, beta)` pair.
    dtype : {'float16', 'float32', 'float64'}, optional
        Data type of output samples. Default is 'float32'
    ctx : Context, optional
        Device context of output. Default is current context. Overridden by
        `alpha.context` when `alpha` is an NDArray.
    out : NDArray, optional
        Store output to an existing NDArray.

    Returns
    -------
    NDArray
        If input `shape` has shape, e.g., `(m, n)` and `alpha` and `beta` are scalars, output
        shape will be `(m, n)`. If `alpha` and `beta` are NDArrays with shape, e.g.,
        `(x, y)`, then output will have shape `(x, y, m, n)`, where `m*n` samples are
        drawn for each `[alpha, beta)` pair.

    Examples
    --------
    >>> mx.nd.random.gamma(1, 1)
    [ 1.93308783]
    <NDArray 1 @cpu(0)>
    >>> mx.nd.random.gamma(1, 1, shape=(2,))
    [ 0.48216391  2.09890771]
    <NDArray 2 @cpu(0)>
    >>> alpha = mx.nd.array([1,2,3])
    >>> beta = mx.nd.array([2,3,4])
    >>> mx.nd.random.gamma(alpha, beta, shape=2)
    [[  3.24343276   0.94137681]
     [  3.52734375   0.45568955]
     [ 14.26264095  14.0170126 ]]
    <NDArray 3x2 @cpu(0)>
    """
    return _random_helper(_internal._random_gamma, _internal._sample_gamma,
                          [alpha, beta], shape, dtype, ctx, out, kwargs)