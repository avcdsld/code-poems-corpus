def pow(base, exp):
    """Returns element-wise result of base element raised to powers from exp element.

    Both inputs can be Symbol or scalar number.
    Broadcasting is not supported. Use `broadcast_pow` instead.

    `sym.pow` is being deprecated, please use `sym.power` instead.

    Parameters
    ---------
    base : Symbol or scalar
        The base symbol
    exp : Symbol or scalar
        The exponent symbol

    Returns
    -------
    Symbol or scalar
        The bases in x raised to the exponents in y.

    Examples
    --------
    >>> mx.sym.pow(2, 3)
    8
    >>> x = mx.sym.Variable('x')
    >>> y = mx.sym.Variable('y')
    >>> z = mx.sym.pow(x, 2)
    >>> z.eval(x=mx.nd.array([1,2]))[0].asnumpy()
    array([ 1.,  4.], dtype=float32)
    >>> z = mx.sym.pow(3, y)
    >>> z.eval(y=mx.nd.array([2,3]))[0].asnumpy()
    array([  9.,  27.], dtype=float32)
    >>> z = mx.sym.pow(x, y)
    >>> z.eval(x=mx.nd.array([3,4]), y=mx.nd.array([2,3]))[0].asnumpy()
    array([  9.,  64.], dtype=float32)
    """
    if isinstance(base, Symbol) and isinstance(exp, Symbol):
        return _internal._Power(base, exp)
    if isinstance(base, Symbol) and isinstance(exp, Number):
        return _internal._PowerScalar(base, scalar=exp)
    if isinstance(base, Number) and isinstance(exp, Symbol):
        return _internal._RPowerScalar(exp, scalar=base)
    if isinstance(base, Number) and isinstance(exp, Number):
        return base**exp
    else:
        raise TypeError('types (%s, %s) not supported' % (str(type(base)), str(type(exp))))