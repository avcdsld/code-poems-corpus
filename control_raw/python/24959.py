def _bdev(dev=None):
    '''
    Resolve a bcacheX or cache to a real dev
    :return: basename of bcache dev
    '''
    if dev is None:
        dev = _fssys('cache0')
    else:
        dev = _bcpath(dev)

    if not dev:
        return False
    else:
        return _devbase(os.path.dirname(dev))