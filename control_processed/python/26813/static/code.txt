def get_selections(fetchempty=True):
    '''
    Answers to debconf questions for all packages in the following format::

        {'package': [['question', 'type', 'value'], ...]}

    CLI Example:

    .. code-block:: bash

        salt '*' debconf.get_selections
    '''
    selections = {}
    cmd = 'debconf-get-selections'

    out = __salt__['cmd.run_stdout'](cmd)

    lines = _unpack_lines(out)

    for line in lines:
        package, question, type_, value = line
        if fetchempty or value:
            (selections
                .setdefault(package, [])
                .append([question, type_, value]))

    return selections