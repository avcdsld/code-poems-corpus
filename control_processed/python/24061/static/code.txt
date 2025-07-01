def update_git_repos(clean=False):
    '''
    Checkout git repos containing :ref:`Windows Software Package Definitions
    <windows-package-manager>`.

    .. important::
        This function requires `Git for Windows`_ to be installed in order to
        work. When installing, make sure to select an installation option which
        permits the git executable to be run from the Command Prompt.

    .. _`Git for Windows`: https://git-for-windows.github.io/

    clean : False
        Clean repo cachedirs which are not configured under
        :conf_minion:`winrepo_remotes`.

        .. note::
            This option only applies if either pygit2_ or GitPython_ is
            installed into Salt's bundled Python.

        .. warning::
            This argument should not be set to ``True`` if a mix of git and
            non-git repo definitions are being used, as it will result in the
            non-git repo definitions being removed.

        .. versionadded:: 2015.8.0

        .. _GitPython: https://github.com/gitpython-developers/GitPython
        .. _pygit2: https://github.com/libgit2/pygit2

    CLI Example:

    .. code-block:: bash

        salt-call winrepo.update_git_repos
    '''
    if not salt.utils.path.which('git'):
        raise CommandExecutionError(
            'Git for Windows is not installed, or not configured to be '
            'accessible from the Command Prompt'
        )
    return _update_git_repos(opts=__opts__, clean=clean, masterless=True)