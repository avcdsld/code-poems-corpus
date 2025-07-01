def install(name=None, refresh=False, pkgs=None, version=None, test=False, **kwargs):
    '''
    Install the named fileset(s)/rpm package(s).

    name
        The name of the fileset or rpm package to be installed.

    refresh
        Whether or not to update the yum database before executing.


    Multiple Package Installation Options:

    pkgs
        A list of filesets and/or rpm packages to install.
        Must be passed as a python list. The ``name`` parameter will be
        ignored if this option is passed.

    version
        Install a specific version of a fileset/rpm package.
        (Unused at present).

    test
        Verify that command functions correctly:

    Returns a dict containing the new fileset(s)/rpm package(s) names and versions:

        {'<package>': {'old': '<old-version>',
                       'new': '<new-version>'}}

    CLI Example:

    .. code-block:: bash

        salt '*' pkg.install /stage/middleware/AIX/bash-4.2-3.aix6.1.ppc.rpm
        salt '*' pkg.install /stage/middleware/AIX/bash-4.2-3.aix6.1.ppc.rpm refresh=True
        salt '*' pkg.install /stage/middleware/AIX/VIOS2211_update/tpc_4.1.1.85.bff
        salt '*' pkg.install /stage/middleware/AIX/Xlc/usr/sys/inst.images/xlC.rte
        salt '*' pkg.install /stage/middleware/AIX/Firefox/ppc-AIX53/Firefox.base
        salt '*' pkg.install pkgs='["foo", "bar"]'
    '''
    targets = salt.utils.args.split_input(pkgs) if pkgs else [name]
    if not targets:
        return {}

    if pkgs:
        log.debug('Removing these fileset(s)/rpm package(s) %s: %s', name, targets)

    # Get a list of the currently installed pkgs.
    old = list_pkgs()

    # Install the fileset or rpm package(s)
    errors = []
    for target in targets:
        filename = os.path.basename(target)
        if filename.endswith('.rpm'):
            if _is_installed_rpm(filename.split('.aix')[0]):
                continue

            cmdflags = ' -Uivh '
            if test:
                cmdflags += ' --test'

            cmd = ['/usr/bin/rpm', cmdflags, target]
            out = __salt__['cmd.run_all'](cmd, output_loglevel='trace')
        else:
            if _is_installed(target):
                continue

            cmd = '/usr/sbin/installp -acYXg'
            if test:
                cmd += 'p'
            cmd += ' -d '
            dirpath = os.path.dirname(target)
            cmd += dirpath +' '+ filename
            out = __salt__['cmd.run_all'](cmd, output_loglevel='trace')

        if 0 != out['retcode']:
            errors.append(out['stderr'])

    # Get a list of the packages after the uninstall
    __context__.pop('pkg.list_pkgs', None)
    new = list_pkgs()
    ret = salt.utils.data.compare_dicts(old, new)

    if errors:
        raise CommandExecutionError(
            'Problems encountered installing filesets(s)/package(s)',
            info={
                'changes': ret,
                'errors': errors
            }
        )

    # No error occurred
    if test:
        return 'Test succeeded.'

    return ret