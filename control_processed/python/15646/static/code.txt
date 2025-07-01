def create(graph, reset_probability=0.15,
           threshold=1e-2,
           max_iterations=20,
           _single_precision=False,
           _distributed='auto',
           verbose=True):
    """
    Compute the PageRank for each vertex in the graph. Return a model object
    with total PageRank as well as the PageRank value for each vertex in the
    graph.

    Parameters
    ----------
    graph : SGraph
        The graph on which to compute the pagerank value.

    reset_probability : float, optional
        Probability that a random surfer jumps to an arbitrary page.

    threshold : float, optional
        Threshold for convergence, measured in the L1 norm
        (the sum of absolute value) of the delta of each vertex's
        pagerank value.

    max_iterations : int, optional
        The maximum number of iterations to run.

    _single_precision : bool, optional
        If true, running pagerank in single precision. The resulting
        pagerank values may not be accurate for large graph, but
        should run faster and use less memory.

    _distributed : distributed environment, internal

    verbose : bool, optional
        If True, print progress updates.


    Returns
    -------
    out : PagerankModel

    References
    ----------
    - `Wikipedia - PageRank <http://en.wikipedia.org/wiki/PageRank>`_
    - Page, L., et al. (1998) `The PageRank Citation Ranking: Bringing Order to
      the Web <http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf>`_.

    Examples
    --------
    If given an :class:`~turicreate.SGraph` ``g``, we can create
    a :class:`~turicreate.pagerank.PageRankModel` as follows:

    >>> g = turicreate.load_sgraph('http://snap.stanford.edu/data/email-Enron.txt.gz', format='snap')
    >>> pr = turicreate.pagerank.create(g)

    We can obtain the page rank corresponding to each vertex in the graph ``g``
    using:

    >>> pr_out = pr['pagerank']     # SFrame

    We can add the new pagerank field to the original graph g using:

    >>> g.vertices['pagerank'] = pr['graph'].vertices['pagerank']

    Note that the task above does not require a join because the vertex
    ordering is preserved through ``create()``.

    See Also
    --------
    PagerankModel
    """
    from turicreate._cython.cy_server import QuietProgress

    if not isinstance(graph, _SGraph):
        raise TypeError('graph input must be a SGraph object.')

    opts = {'threshold': threshold, 'reset_probability': reset_probability,
            'max_iterations': max_iterations,
            'single_precision': _single_precision,
            'graph': graph.__proxy__}

    with QuietProgress(verbose):
        params = _tc.extensions._toolkits.graph.pagerank.create(opts)
    model = params['model']

    return PagerankModel(model)