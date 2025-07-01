def grant_access_to_shared_folders_to(name, users=None):
    '''
    Grant access to auto-mounted shared folders to the users.

    User is specified by it's name. To grant access for several users use argument `users`.
    Access will be denied to the users not listed in `users` argument.

    See https://www.virtualbox.org/manual/ch04.html#sf_mount_auto for more details.

    CLI Example:

    .. code-block:: bash

        salt '*' vbox_guest.grant_access_to_shared_folders_to fred
        salt '*' vbox_guest.grant_access_to_shared_folders_to users ['fred', 'roman']

    :param name: name of the user to grant access to auto-mounted shared folders to
    :type name: str
    :param users: list of names of users to grant access to auto-mounted shared folders to (if specified, `name` will not be taken into account)
    :type users: list of str
    :return: list of users who have access to auto-mounted shared folders
    '''
    if users is None:
        users = [name]
    if __salt__['group.members'](_shared_folders_group, ','.join(users)):
        return users
    else:
        if not __salt__['group.info'](_shared_folders_group):
            if not additions_version:
                return ("VirtualBox Guest Additions are not installed. Ιnstall "
                        "them firstly. You can do it with the help of command "
                        "vbox_guest.additions_install.")
            else:
                return (
                    "VirtualBox Guest Additions seems to be installed, but "
                    "group '{0}' not found. Check your installation and fix "
                    "it. You can uninstall VirtualBox Guest Additions with "
                    "the help of command :py:func:`vbox_guest.additions_remove "
                    "<salt.modules.vbox_guest.additions_remove> (it has "
                    "`force` argument to fix complex situations; use "
                    "it with care) and then install it again. You can do "
                    "it with the help of :py:func:`vbox_guest.additions_install "
                    "<salt.modules.vbox_guest.additions_install>`."
                    "".format(_shared_folders_group))
        else:
            return ("Cannot replace members of the '{0}' group."
                    "".format(_shared_folders_group))