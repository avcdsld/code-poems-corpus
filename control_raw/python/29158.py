def netmiko_commands(*commands, **kwargs):
    '''
    .. versionadded:: 2019.2.0

    Invoke one or more commands to be executed on the remote device, via Netmiko.
    Returns a list of strings, with the output from each command.

    commands
        A list of commands to be executed.

    expect_string
        Regular expression pattern to use for determining end of output.
        If left blank will default to being based on router prompt.

    delay_factor: ``1``
        Multiplying factor used to adjust delays (default: ``1``).

    max_loops: ``500``
        Controls wait time in conjunction with delay_factor. Will default to be
        based upon self.timeout.

    auto_find_prompt: ``True``
        Whether it should try to auto-detect the prompt (default: ``True``).

    strip_prompt: ``True``
        Remove the trailing router prompt from the output (default: ``True``).

    strip_command: ``True``
        Remove the echo of the command from the output (default: ``True``).

    normalize: ``True``
        Ensure the proper enter is sent at end of command (default: ``True``).

    use_textfsm: ``False``
        Process command output through TextFSM template (default: ``False``).

    CLI Example:

    .. code-block:: bash

        salt '*' napalm.netmiko_commands 'show version' 'show interfaces'
    '''
    conn = netmiko_conn(**kwargs)
    ret = []
    for cmd in commands:
        ret.append(conn.send_command(cmd))
    return ret