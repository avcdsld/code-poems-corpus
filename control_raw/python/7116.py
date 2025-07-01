def makedirs(d):
    """Create directories recursively if they don't exist. os.makedirs(exist_ok=True) is not
    available in Python2"""
    if sys.version_info[0] < 3:
        from distutils.dir_util import mkpath
        mkpath(d)
    else:
        os.makedirs(d, exist_ok=True)