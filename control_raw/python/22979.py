def delete_config(lines, **kwargs):
    '''
    Delete one or more config lines to the switch running config.

    lines
        Configuration lines to remove.

    no_save_config
        If True, don't save configuration commands to startup configuration.
        If False, save configuration to startup configuration.
        Default: False

    .. code-block:: bash

        salt '*' nxos.cmd delete_config 'snmp-server community TESTSTRINGHERE group network-operator'

    .. note::
        For more than one config deleted per command, lines should be a list.
    '''
    if not isinstance(lines, list):
        lines = [lines]
    for i, _ in enumerate(lines):
        lines[i] = 'no ' + lines[i]
    result = None
    try:
        result = config(lines, **kwargs)
    except CommandExecutionError as e:
        # Some commands will generate error code 400 if they do not exist
        # and we try to remove them.  These can be ignored.
        if ast.literal_eval(e.message)['code'] != '400':
            raise
    return result