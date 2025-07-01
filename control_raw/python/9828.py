def filter_pythons(path):
    # type: (Union[str, vistir.compat.Path]) -> Iterable
    """Return all valid pythons in a given path"""
    if not isinstance(path, vistir.compat.Path):
        path = vistir.compat.Path(str(path))
    if not path.is_dir():
        return path if path_is_python(path) else None
    return filter(path_is_python, path.iterdir())