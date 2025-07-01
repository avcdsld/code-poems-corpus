def glob_in_parents(dir, patterns, upper_limit=None):
    """Recursive version of GLOB which glob sall parent directories
    of dir until the first match is found. Returns an empty result if no match
    is found"""

    assert(isinstance(dir, str))
    assert(isinstance(patterns, list))

    result = []

    absolute_dir = os.path.join(os.getcwd(), dir)
    absolute_dir = os.path.normpath(absolute_dir)
    while absolute_dir:
        new_dir = os.path.split(absolute_dir)[0]
        if new_dir == absolute_dir:
            break
        result = glob([new_dir], patterns)
        if result:
            break
        absolute_dir = new_dir

    return result