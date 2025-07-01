def _get_build_env(env):
    '''
    Get build environment overrides dictionary to use in build process
    '''
    env_override = ''
    if env is None:
        return env_override
    if not isinstance(env, dict):
        raise SaltInvocationError(
            '\'env\' must be a Python dictionary'
        )
    for key, value in env.items():
        env_override += '{0}={1}\n'.format(key, value)
        env_override += 'export {0}\n'.format(key)
    return env_override