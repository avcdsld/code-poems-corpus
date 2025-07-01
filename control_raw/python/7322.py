def empty(stype, shape, ctx=None, dtype=None):
    """Returns a new array of given shape and type, without initializing entries.

    Parameters
    ----------
    stype: string
        The storage type of the empty array, such as 'row_sparse', 'csr', etc
    shape : int or tuple of int
        The shape of the empty array.
    ctx : Context, optional
        An optional device context (default is the current default context).
    dtype : str or numpy.dtype, optional
        An optional value type (default is `float32`).

    Returns
    -------
    CSRNDArray or RowSparseNDArray
        A created array.
    """
    if isinstance(shape, int):
        shape = (shape, )
    if ctx is None:
        ctx = current_context()
    if dtype is None:
        dtype = mx_real_t
    assert(stype is not None)
    if stype in ('csr', 'row_sparse'):
        return zeros(stype, shape, ctx=ctx, dtype=dtype)
    else:
        raise Exception("unknown stype : " + str(stype))