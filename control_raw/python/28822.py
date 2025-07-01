def remove(name=None, pkgs=None, purge=False, **kwargs):
    '''
    Remove a single package with pkg_delete

    Multiple Package Options:

    pkgs
        A list of packages to delete. Must be passed as a python list. The
        ``name`` parameter will be ignored if this option is passed.

    .. versionadded:: 0.16.0


    Returns a dict containing the changes.

    CLI Example:

    .. code-block:: bash

        salt '*' pkg.remove <package name>
        salt '*' pkg.remove <package1>,<package2>,<package3>
        salt '*' pkg.remove pkgs='["foo", "bar"]'
    '''
    try:
        pkg_params = [x.split('--')[0] for x in
                      __salt__['pkg_resource.parse_targets'](name, pkgs)[0]]
    except MinionError as exc:
        raise CommandExecutionError(exc)

    old = list_pkgs()
    targets = [x for x in pkg_params if x in old]
    if not targets:
        return {}

    cmd = ['pkg_delete', '-Ix', '-Ddependencies']

    if purge:
        cmd.append('-cqq')

    cmd.extend(targets)

    out = __salt__['cmd.run_all'](
        cmd,
        python_shell=False,
        output_loglevel='trace'
    )
    if out['retcode'] != 0 and out['stderr']:
        errors = [out['stderr']]
    else:
        errors = []

    __context__.pop('pkg.list_pkgs', None)
    new = list_pkgs()
    ret = salt.utils.data.compare_dicts(old, new)

    if errors:
        raise CommandExecutionError(
            'Problem encountered removing package(s)',
            info={'errors': errors, 'changes': ret}
        )

    return ret