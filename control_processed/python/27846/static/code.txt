def cmd(command, *args, **kwargs):
    '''
    run commands from __proxy__
    :mod:`salt.proxy.onyx<salt.proxy.onyx>`

    command
        function from `salt.proxy.onyx` to run

    args
        positional args to pass to `command` function

    kwargs
        key word arguments to pass to `command` function

    .. code-block:: bash

        salt '*' onyx.cmd sendline 'show ver'
        salt '*' onyx.cmd show_run
        salt '*' onyx.cmd check_password username=admin
        password='$5$lkjsdfoi$blahblahblah' encrypted=True
    '''
    proxy_prefix = __opts__['proxy']['proxytype']
    proxy_cmd = '.'.join([proxy_prefix, command])
    if proxy_cmd not in __proxy__:
        return False
    for k in list(kwargs):
        if k.startswith('__pub_'):
            kwargs.pop(k)
    return __proxy__[proxy_cmd](*args, **kwargs)