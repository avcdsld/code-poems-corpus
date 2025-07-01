def factory(opts, **kwargs):
    '''
    Creates and returns the cache class.
    If memory caching is enabled by opts MemCache class will be instantiated.
    If not Cache class will be returned.
    '''
    if opts.get('memcache_expire_seconds', 0):
        cls = MemCache
    else:
        cls = Cache
    return cls(opts, **kwargs)