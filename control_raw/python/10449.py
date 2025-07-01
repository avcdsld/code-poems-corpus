def set_attribute(name, value):
    """
    Decorator factory for setting attributes on a function.

    Doesn't change the behavior of the wrapped function.

    Examples
    --------
    >>> @set_attribute('__name__', 'foo')
    ... def bar():
    ...     return 3
    ...
    >>> bar()
    3
    >>> bar.__name__
    'foo'
    """
    def decorator(f):
        setattr(f, name, value)
        return f
    return decorator