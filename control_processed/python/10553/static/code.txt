def templated_docstring(**docs):
    """
    Decorator allowing the use of templated docstrings.

    Examples
    --------
    >>> @templated_docstring(foo='bar')
    ... def my_func(self, foo):
    ...     '''{foo}'''
    ...
    >>> my_func.__doc__
    'bar'
    """
    def decorator(f):
        f.__doc__ = format_docstring(f.__name__, f.__doc__, docs)
        return f
    return decorator