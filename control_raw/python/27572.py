def remove(name=None, pkgs=None, **kwargs):
    '''
    Remove specified fileset(s)/rpm package(s).

    name
        The name of the fileset or rpm package to be deleted.


    Multiple Package Options:

    pkgs
        A list of filesets and/or rpm packages to delete.
        Must be passed as a python list. The ``name`` parameter will be
        ignored if this option is passed.


    Returns a list containing the removed packages.

    CLI Example:

    .. code-block:: bash

        salt '*' pkg.remove <fileset/rpm package name>
        salt '*' pkg.remove tcsh
        salt '*' pkg.remove xlC.rte
        salt '*' pkg.remove Firefox.base.adt
        salt '*' pkg.remove pkgs='["foo", "bar"]'
    '''
    targets = salt.utils.args.split_input(pkgs) if pkgs else [name]
    if not targets:
        return {}

    if pkgs:
        log.debug('Removing these fileset(s)/rpm package(s) %s: %s', name, targets)

    errors = []

    # Get a list of the currently installed pkgs.
    old = list_pkgs()

    # Remove the fileset or rpm package(s)
    for target in targets:
        try:
            named, versionpkg, rpmpkg = _check_pkg(target)
        except CommandExecutionError as exc:
            if exc.info:
                errors.append(exc.info['errors'])
            continue

        if rpmpkg:
            cmd = ['/usr/bin/rpm', '-e', named]
            out = __salt__['cmd.run_all'](cmd, output_loglevel='trace')
        else:
            cmd = ['/usr/sbin/installp', '-u', named]
            out = __salt__['cmd.run_all'](cmd, output_loglevel='trace')

    # Get a list of the packages after the uninstall
    __context__.pop('pkg.list_pkgs', None)
    new = list_pkgs()
    ret = salt.utils.data.compare_dicts(old, new)

    if errors:
        raise CommandExecutionError(
            'Problems encountered removing filesets(s)/package(s)',
            info={
                'changes': ret,
                'errors': errors
            }
        )

    return ret