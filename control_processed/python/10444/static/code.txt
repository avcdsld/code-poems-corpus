def same(*values):
    """
    Check if all values in a sequence are equal.

    Returns True on empty sequences.

    Examples
    --------
    >>> same(1, 1, 1, 1)
    True
    >>> same(1, 2, 1)
    False
    >>> same()
    True
    """
    if not values:
        return True
    first, rest = values[0], values[1:]
    return all(value == first for value in rest)