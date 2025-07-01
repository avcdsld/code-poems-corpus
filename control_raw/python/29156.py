def netmiko_call(method, *args, **kwargs):
    '''
    .. versionadded:: 2019.2.0

    Execute an arbitrary Netmiko method, passing the authentication details from
    the existing NAPALM connection.

    method
        The name of the Netmiko method to execute.

    args
        List of arguments to send to the Netmiko method specified in ``method``.

    kwargs
        Key-value arguments to send to the execution function specified in
        ``method``.

    CLI Example:

    .. code-block:: bash

        salt '*' napalm.netmiko_call send_command 'show version'
    '''
    netmiko_kwargs = netmiko_args()
    kwargs.update(netmiko_kwargs)
    return __salt__['netmiko.call'](method, *args, **kwargs)