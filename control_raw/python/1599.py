def dispatch_to_index_op(op, left, right, index_class):
    """
    Wrap Series left in the given index_class to delegate the operation op
    to the index implementation.  DatetimeIndex and TimedeltaIndex perform
    type checking, timezone handling, overflow checks, etc.

    Parameters
    ----------
    op : binary operator (operator.add, operator.sub, ...)
    left : Series
    right : object
    index_class : DatetimeIndex or TimedeltaIndex

    Returns
    -------
    result : object, usually DatetimeIndex, TimedeltaIndex, or Series
    """
    left_idx = index_class(left)

    # avoid accidentally allowing integer add/sub.  For datetime64[tz] dtypes,
    # left_idx may inherit a freq from a cached DatetimeIndex.
    # See discussion in GH#19147.
    if getattr(left_idx, 'freq', None) is not None:
        left_idx = left_idx._shallow_copy(freq=None)
    try:
        result = op(left_idx, right)
    except NullFrequencyError:
        # DatetimeIndex and TimedeltaIndex with freq == None raise ValueError
        # on add/sub of integers (or int-like).  We re-raise as a TypeError.
        raise TypeError('incompatible type for a datetime/timedelta '
                        'operation [{name}]'.format(name=op.__name__))
    return result