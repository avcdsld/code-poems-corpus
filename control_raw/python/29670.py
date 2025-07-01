def get_mirror(name, config_path=_DEFAULT_CONFIG_PATH, with_packages=False):
    '''
    Get detailed information about a mirrored remote repository.

    :param str name: The name of the remote repository mirror.
    :param str config_path: The path to the configuration file for the aptly instance.
    :param bool with_packages: Return a list of packages in the repo.

    :return: A dictionary containing information about the mirror.
    :rtype: dict

    CLI Example:

    .. code-block:: bash

        salt '*' aptly.get_mirror name="test-mirror"
    '''
    _validate_config(config_path)

    ret = dict()
    cmd = ['mirror', 'show', '-config={}'.format(config_path),
           '-with-packages={}'.format(str(with_packages).lower()),
           name]

    cmd_ret = _cmd_run(cmd)

    ret = _parse_show_output(cmd_ret=cmd_ret)

    if ret:
        log.debug('Found mirror: %s', name)
    else:
        log.debug('Unable to find mirror: %s', name)

    return ret