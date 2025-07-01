def check_env_cache(opts, env_cache):
    '''
    Returns cached env names, if present. Otherwise returns None.
    '''
    if not os.path.isfile(env_cache):
        return None
    try:
        with salt.utils.files.fopen(env_cache, 'rb') as fp_:
            log.trace('Returning env cache data from %s', env_cache)
            serial = salt.payload.Serial(opts)
            return salt.utils.data.decode(serial.load(fp_))
    except (IOError, OSError):
        pass
    return None