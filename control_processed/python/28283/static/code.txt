def _trim_env_off_path(paths, saltenv, trim_slash=False):
    '''
    Return a list of file paths with the saltenv directory removed
    '''
    env_len = None if _is_env_per_bucket() else len(saltenv) + 1
    slash_len = -1 if trim_slash else None

    return [d[env_len:slash_len] for d in paths]