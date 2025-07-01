def _gem(command, ruby=None, runas=None, gem_bin=None):
    '''
    Run the actual gem command. If rvm or rbenv is installed, run the command
    using the corresponding module. rbenv is not available on windows, so don't
    try.

    :param command: string
    Command to run
    :param ruby: string : None
    If RVM or rbenv are installed, the ruby version and gemset to use.
    Ignored if ``gem_bin`` is specified.
    :param runas: string : None
    The user to run gem as.
    :param gem_bin: string : None
    Full path to the ``gem`` binary

    :return:
    Returns the full standard out including success codes or False if it fails
    '''
    cmdline = [gem_bin or 'gem'] + command

    # If a custom gem is given, use that and don't check for rvm/rbenv. User
    # knows best!
    if gem_bin is None:
        if __salt__['rvm.is_installed'](runas=runas):
            return __salt__['rvm.do'](ruby, cmdline, runas=runas)

        if not salt.utils.platform.is_windows() \
                and __salt__['rbenv.is_installed'](runas=runas):
            if ruby is None:
                return __salt__['rbenv.do'](cmdline, runas=runas)
            else:
                return __salt__['rbenv.do_with_ruby'](ruby,
                                                      cmdline,
                                                      runas=runas)

    ret = __salt__['cmd.run_all'](cmdline, runas=runas, python_shell=False)

    if ret['retcode'] == 0:
        return ret['stdout']
    else:
        raise CommandExecutionError(ret['stderr'])