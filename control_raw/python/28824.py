def upgrade(name=None,
            pkgs=None,
            **kwargs):
    '''
    Run a full package upgrade (``pkg_add -u``), or upgrade a specific package
    if ``name`` or ``pkgs`` is provided.
    ``name`` is ignored when ``pkgs`` is specified.

    Returns a dictionary containing the changes:

    .. versionadded:: 2019.2.0

    .. code-block:: python

        {'<package>': {'old': '<old-version>',
                       'new': '<new-version>'}}

    CLI Example:

    .. code-block:: bash

        salt '*' pkg.upgrade
        salt '*' pkg.upgrade python%2.7
    '''
    old = list_pkgs()

    cmd = ['pkg_add', '-Ix', '-u']

    if kwargs.get('noop', False):
        cmd.append('-n')

    if pkgs:
        cmd.extend(pkgs)
    elif name:
        cmd.append(name)

    # Now run the upgrade, compare the list of installed packages before and
    # after and we have all the info we need.
    result = __salt__['cmd.run_all'](cmd, output_loglevel='trace',
                                     python_shell=False)

    __context__.pop('pkg.list_pkgs', None)
    new = list_pkgs()
    ret = salt.utils.data.compare_dicts(old, new)

    if result['retcode'] != 0:
        raise CommandExecutionError(
                'Problem encountered upgrading packages',
                info={'changes': ret, 'result': result}
        )

    return ret