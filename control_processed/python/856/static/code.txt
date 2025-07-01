def _interp_limit(invalid, fw_limit, bw_limit):
    """
    Get indexers of values that won't be filled
    because they exceed the limits.

    Parameters
    ----------
    invalid : boolean ndarray
    fw_limit : int or None
        forward limit to index
    bw_limit : int or None
        backward limit to index

    Returns
    -------
    set of indexers

    Notes
    -----
    This is equivalent to the more readable, but slower

    .. code-block:: python

        def _interp_limit(invalid, fw_limit, bw_limit):
            for x in np.where(invalid)[0]:
                if invalid[max(0, x - fw_limit):x + bw_limit + 1].all():
                    yield x
    """
    # handle forward first; the backward direction is the same except
    # 1. operate on the reversed array
    # 2. subtract the returned indices from N - 1
    N = len(invalid)
    f_idx = set()
    b_idx = set()

    def inner(invalid, limit):
        limit = min(limit, N)
        windowed = _rolling_window(invalid, limit + 1).all(1)
        idx = (set(np.where(windowed)[0] + limit) |
               set(np.where((~invalid[:limit + 1]).cumsum() == 0)[0]))
        return idx

    if fw_limit is not None:

        if fw_limit == 0:
            f_idx = set(np.where(invalid)[0])
        else:
            f_idx = inner(invalid, fw_limit)

    if bw_limit is not None:

        if bw_limit == 0:
            # then we don't even need to care about backwards
            # just use forwards
            return f_idx
        else:
            b_idx = list(inner(invalid[::-1], bw_limit))
            b_idx = set(N - 1 - np.asarray(b_idx))
            if fw_limit == 0:
                return b_idx

    return f_idx & b_idx