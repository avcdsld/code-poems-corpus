def looks_like_python(name):
    # type: (str) -> bool
    """
    Determine whether the supplied filename looks like a possible name of python.

    :param str name: The name of the provided file.
    :return: Whether the provided name looks like python.
    :rtype: bool
    """

    if not any(name.lower().startswith(py_name) for py_name in PYTHON_IMPLEMENTATIONS):
        return False
    match = RE_MATCHER.match(name)
    if match:
        return any(fnmatch(name, rule) for rule in MATCH_RULES)
    return False