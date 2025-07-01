def _factorize_from_iterables(iterables):
    """
    A higher-level wrapper over `_factorize_from_iterable`.

    *This is an internal function*

    Parameters
    ----------
    iterables : list-like of list-likes

    Returns
    -------
    codes_list : list of ndarrays
    categories_list : list of Indexes

    Notes
    -----
    See `_factorize_from_iterable` for more info.
    """
    if len(iterables) == 0:
        # For consistency, it should return a list of 2 lists.
        return [[], []]
    return map(list, lzip(*[_factorize_from_iterable(it) for it in iterables]))