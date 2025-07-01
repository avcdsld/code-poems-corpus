def find_objects(config=None, config_path=None, regex=None, saltenv='base'):
    '''
    Return all the line objects that match the expression in the ``regex``
    argument.

    .. warning::
        This function is mostly valuable when invoked from other Salt
        components (i.e., execution modules, states, templates etc.). For CLI
        usage, please consider using
        :py:func:`ciscoconfparse.find_lines <salt.ciscoconfparse_mod.find_lines>`

    config
        The configuration sent as text.

        .. note::
            This argument is ignored when ``config_path`` is specified.

    config_path
        The absolute or remote path to the file with the configuration to be
        parsed. This argument supports the usual Salt filesystem URIs, e.g.,
        ``salt://``, ``https://``, ``ftp://``, ``s3://``, etc.

    regex
        The regular expression to match the lines against.

    saltenv: ``base``
        Salt fileserver environment from which to retrieve the file. This
        argument is ignored when ``config_path`` is not a ``salt://`` URL.

    Usage example:

    .. code-block:: python

        objects = __salt__['ciscoconfparse.find_objects'](config_path='salt://path/to/config.txt',
                                                          regex='Gigabit')
        for obj in objects:
            print(obj.text)
    '''
    ccp = _get_ccp(config=config, config_path=config_path, saltenv=saltenv)
    lines = ccp.find_objects(regex)
    return lines