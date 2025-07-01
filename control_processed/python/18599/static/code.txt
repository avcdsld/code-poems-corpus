def linear(m=1, b=0):
    ''' Return a driver function that can advance a sequence of linear values.

    .. code-block:: none

        value = m * i + b

    Args:
        m (float) : a slope for the linear driver
        x (float) : an offset for the linear driver

    '''
    def f(i):
        return m * i + b
    return partial(force, sequence=_advance(f))