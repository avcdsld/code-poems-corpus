def runner(fun, arg=None, timeout=5):
    '''
    Execute a runner on the master and return the data from the runnr function

    CLI Example:

    .. code-block:: bash

        salt-ssh '*' publish.runner jobs.lookup_jid 20140916125524463507
    '''
    # Form args as list
    if not isinstance(arg, list):
        arg = [salt.utils.args.yamlify_arg(arg)]
    else:
        arg = [salt.utils.args.yamlify_arg(x) for x in arg]
    if len(arg) == 1 and arg[0] is None:
        arg = []

    # Create and run the runner
    runner = salt.runner.RunnerClient(__opts__['__master_opts__'])
    return runner.cmd(fun, arg)