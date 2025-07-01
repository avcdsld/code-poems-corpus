def select_highest_ranked (elements, ranks):
    """ Returns all of 'elements' for which corresponding element in parallel
        list 'rank' is equal to the maximum value in 'rank'.
    """
    assert is_iterable(elements)
    assert is_iterable(ranks)
    if not elements:
        return []

    max_rank = max_element (ranks)

    result = []
    while elements:
        if ranks [0] == max_rank:
            result.append (elements [0])

        elements = elements [1:]
        ranks = ranks [1:]

    return result