def _get_pip_bin(bin_env):
    '''
    Locate the pip binary, either from `bin_env` as a virtualenv, as the
    executable itself, or from searching conventional filesystem locations
    '''
    if not bin_env:
        logger.debug('pip: Using pip from currently-running Python')
        return [os.path.normpath(sys.executable), '-m', 'pip']

    python_bin = 'python.exe' if salt.utils.platform.is_windows() else 'python'

    def _search_paths(*basedirs):
        ret = []
        for path in basedirs:
            ret.extend([
                os.path.join(path, python_bin),
                os.path.join(path, 'bin', python_bin),
                os.path.join(path, 'Scripts', python_bin)
            ])
        return ret

    # try to get python bin from virtualenv (i.e. bin_env)
    if os.path.isdir(bin_env):
        for bin_path in _search_paths(bin_env):
            if os.path.isfile(bin_path):
                if os.access(bin_path, os.X_OK):
                    logger.debug('pip: Found python binary: %s', bin_path)
                    return [os.path.normpath(bin_path), '-m', 'pip']
                else:
                    logger.debug(
                        'pip: Found python binary by name but it is not '
                        'executable: %s', bin_path
                    )
        raise CommandNotFoundError(
            'Could not find a pip binary in virtualenv {0}'.format(bin_env)
        )

    # bin_env is the python or pip binary
    elif os.access(bin_env, os.X_OK):
        if os.path.isfile(bin_env):
            # If the python binary was passed, return it
            if 'python' in os.path.basename(bin_env):
                return [os.path.normpath(bin_env), '-m', 'pip']
            # We have been passed a pip binary, use the pip binary.
            return [os.path.normpath(bin_env)]

        raise CommandExecutionError(
            'Could not find a pip binary within {0}'.format(bin_env)
        )
    else:
        raise CommandNotFoundError(
            'Access denied to {0}, could not find a pip binary'.format(bin_env)
        )