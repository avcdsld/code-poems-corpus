def file_hash(load, fnd):
    '''
    Return a file hash, the hash type is set in the master config file
    '''
    if 'env' in load:
        # "env" is not supported; Use "saltenv".
        load.pop('env')

    if not all(x in load for x in ('path', 'saltenv')):
        return ''
    saltenv = load['saltenv']
    if saltenv == 'base':
        saltenv = 'trunk'
    ret = {}
    relpath = fnd['rel']
    path = fnd['path']

    # If the file doesn't exist, we can't get a hash
    if not path or not os.path.isfile(path):
        return ret

    # Set the hash_type as it is determined by config
    ret['hash_type'] = __opts__['hash_type']

    # Check if the hash is cached
    # Cache file's contents should be "hash:mtime"
    cache_path = os.path.join(__opts__['cachedir'],
                              'svnfs',
                              'hash',
                              saltenv,
                              '{0}.hash.{1}'.format(relpath,
                                                    __opts__['hash_type']))
    # If we have a cache, serve that if the mtime hasn't changed
    if os.path.exists(cache_path):
        with salt.utils.files.fopen(cache_path, 'rb') as fp_:
            hsum, mtime = fp_.read().split(':')
            if os.path.getmtime(path) == mtime:
                # check if mtime changed
                ret['hsum'] = hsum
                return ret

    # if we don't have a cache entry-- lets make one
    ret['hsum'] = salt.utils.hashutils.get_hash(path, __opts__['hash_type'])
    cache_dir = os.path.dirname(cache_path)
    # make cache directory if it doesn't exist
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    # save the cache object "hash:mtime"
    with salt.utils.files.fopen(cache_path, 'w') as fp_:
        fp_.write('{0}:{1}'.format(ret['hsum'], os.path.getmtime(path)))

    return ret