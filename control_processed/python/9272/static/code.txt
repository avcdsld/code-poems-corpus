def cd(path):
    """Context manager to temporarily change working directories

    :param str path: The directory to move into

    >>> print(os.path.abspath(os.curdir))
    '/home/user/code/myrepo'
    >>> with cd("/home/user/code/otherdir/subdir"):
    ...     print("Changed directory: %s" % os.path.abspath(os.curdir))
    Changed directory: /home/user/code/otherdir/subdir
    >>> print(os.path.abspath(os.curdir))
    '/home/user/code/myrepo'
    """
    if not path:
        return
    prev_cwd = Path.cwd().as_posix()
    if isinstance(path, Path):
        path = path.as_posix()
    os.chdir(str(path))
    try:
        yield
    finally:
        os.chdir(prev_cwd)