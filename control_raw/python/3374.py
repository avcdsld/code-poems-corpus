def is_writable_attr(ext):
    """Check if an extension attribute is writable.
    ext (tuple): The (default, getter, setter, method) tuple available  via
        {Doc,Span,Token}.get_extension.
    RETURNS (bool): Whether the attribute is writable.
    """
    default, method, getter, setter = ext
    # Extension is writable if it has a setter (getter + setter), if it has a
    # default value (or, if its default value is none, none of the other values
    # should be set).
    if setter is not None or default is not None or all(e is None for e in ext):
        return True
    return False