def _cmd(binary, *args):
    '''
    Wrapper to run at(1) or return None.
    '''
    binary = salt.utils.path.which(binary)
    if not binary:
        raise CommandNotFoundError('{0}: command not found'.format(binary))
    cmd = [binary] + list(args)
    return __salt__['cmd.run_stdout']([binary] + list(args),
                                      python_shell=False)