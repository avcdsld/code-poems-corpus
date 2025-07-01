def _check_repo_sign_utils_support(name):
    '''
    Check for specified command name in search path
    '''
    if salt.utils.path.which(name):
        return True
    else:
        raise CommandExecutionError(
            'utility \'{0}\' needs to be installed or made available in search path'.format(name)
        )