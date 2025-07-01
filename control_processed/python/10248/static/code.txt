def constrain (n, min, max):

    '''This returns a number, n constrained to the min and max bounds. '''

    if n < min:
        return min
    if n > max:
        return max
    return n