def delimit(delimiters, content):
    """
    Surround `content` with the first and last characters of `delimiters`.

    >>> delimit('[]', "foo")  # doctest: +SKIP
    '[foo]'
    >>> delimit('""', "foo")  # doctest: +SKIP
    '"foo"'
    """
    if len(delimiters) != 2:
        raise ValueError(
            "`delimiters` must be of length 2. Got %r" % delimiters
        )
    return ''.join([delimiters[0], content, delimiters[1]])