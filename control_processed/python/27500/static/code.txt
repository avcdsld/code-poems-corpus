def delete_user(name, runas=None):
    '''
    Deletes a user via rabbitmqctl delete_user.

    CLI Example:

    .. code-block:: bash

        salt '*' rabbitmq.delete_user rabbit_user
    '''
    if runas is None and not salt.utils.platform.is_windows():
        runas = salt.utils.user.get_user()
    res = __salt__['cmd.run_all'](
        [RABBITMQCTL, 'delete_user', name],
        reset_system_locale=False,
        python_shell=False,
        runas=runas)
    msg = 'Deleted'

    return _format_response(res, msg)