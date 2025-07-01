def normalize_path(path, resolve_symlinks=True):
    # type: (str, bool) -> str
    """
    Convert a path to its canonical, case-normalized, absolute version.

    """
    path = expanduser(path)
    if resolve_symlinks:
        path = os.path.realpath(path)
    else:
        path = os.path.abspath(path)
    return os.path.normcase(path)