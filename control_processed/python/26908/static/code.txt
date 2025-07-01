def fcontext_add_or_delete_policy(action, name, filetype=None, sel_type=None, sel_user=None, sel_level=None):
    '''
    .. versionadded:: 2017.7.0

    Adds or deletes the SELinux policy for a given filespec and other optional parameters.

    Returns the result of the call to semanage.

    Note that you don't have to remove an entry before setting a new
    one for a given filespec and filetype, as adding one with semanage
    automatically overwrites a previously configured SELinux context.

    .. warning::

        Use :mod:`selinux.fcontext_add_policy()<salt.modules.selinux.fcontext_add_policy>`,
        or :mod:`selinux.fcontext_delete_policy()<salt.modules.selinux.fcontext_delete_policy>`.

    .. deprecated:: 2019.2.0

    action
        The action to perform. Either ``add`` or ``delete``.

    name
        filespec of the file or directory. Regex syntax is allowed.

    file_type
        The SELinux filetype specification. Use one of [a, f, d, c, b,
        s, l, p]. See also ``man semanage-fcontext``. Defaults to 'a'
        (all files).

    sel_type
        SELinux context type. There are many.

    sel_user
        SELinux user. Use ``semanage login -l`` to determine which ones
        are available to you.

    sel_level
        The MLS range of the SELinux context.

    CLI Example:

    .. code-block:: bash

        salt '*' selinux.fcontext_add_or_delete_policy add my-policy
    '''
    salt.utils.versions.warn_until(
        'Sodium',
        'The \'selinux.fcontext_add_or_delete_policy\' module has been deprecated. Please use the '
        '\'selinux.fcontext_add_policy\' and \'selinux.fcontext_delete_policy\' modules instead. '
        'Support for the \'selinux.fcontext_add_or_delete_policy\' module will be removed in Salt '
        '{version}.'
    )
    return _fcontext_add_or_delete_policy(action, name, filetype, sel_type, sel_user, sel_level)