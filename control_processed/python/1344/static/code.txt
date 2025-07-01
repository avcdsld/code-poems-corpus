def _union_indexes(indexes, sort=True):
    """
    Return the union of indexes.

    The behavior of sort and names is not consistent.

    Parameters
    ----------
    indexes : list of Index or list objects
    sort : bool, default True
        Whether the result index should come out sorted or not.

    Returns
    -------
    Index
    """
    if len(indexes) == 0:
        raise AssertionError('Must have at least 1 Index to union')
    if len(indexes) == 1:
        result = indexes[0]
        if isinstance(result, list):
            result = Index(sorted(result))
        return result

    indexes, kind = _sanitize_and_check(indexes)

    def _unique_indices(inds):
        """
        Convert indexes to lists and concatenate them, removing duplicates.

        The final dtype is inferred.

        Parameters
        ----------
        inds : list of Index or list objects

        Returns
        -------
        Index
        """
        def conv(i):
            if isinstance(i, Index):
                i = i.tolist()
            return i

        return Index(
            lib.fast_unique_multiple_list([conv(i) for i in inds], sort=sort))

    if kind == 'special':
        result = indexes[0]

        if hasattr(result, 'union_many'):
            return result.union_many(indexes[1:])
        else:
            for other in indexes[1:]:
                result = result.union(other)
            return result
    elif kind == 'array':
        index = indexes[0]
        for other in indexes[1:]:
            if not index.equals(other):

                if sort is None:
                    # TODO: remove once pd.concat sort default changes
                    warnings.warn(_sort_msg, FutureWarning, stacklevel=8)
                    sort = True

                return _unique_indices(indexes)

        name = _get_consensus_names(indexes)[0]
        if name != index.name:
            index = index._shallow_copy(name=name)
        return index
    else:  # kind='list'
        return _unique_indices(indexes)