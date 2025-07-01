def config_changed(inherit_napalm_device=None, **kwargs):  # pylint: disable=unused-argument

    '''
    Will prompt if the configuration has been changed.

    :return: A tuple with a boolean that specifies if the config was changed on the device.\
    And a string that provides more details of the reason why the configuration was not changed.

    CLI Example:

    .. code-block:: bash

        salt '*' net.config_changed
    '''

    is_config_changed = False
    reason = ''
    try_compare = compare_config(inherit_napalm_device=napalm_device)  # pylint: disable=undefined-variable

    if try_compare.get('result'):
        if try_compare.get('out'):
            is_config_changed = True
        else:
            reason = 'Configuration was not changed on the device.'
    else:
        reason = try_compare.get('comment')

    return is_config_changed, reason