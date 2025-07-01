def transform (list, pattern, indices = [1]):
    """ Matches all elements of 'list' agains the 'pattern'
        and returns a list of the elements indicated by indices of
        all successfull matches. If 'indices' is omitted returns
        a list of first paranthethised groups of all successfull
        matches.
    """
    result = []

    for e in list:
        m = re.match (pattern, e)

        if m:
            for i in indices:
                result.append (m.group (i))

    return result