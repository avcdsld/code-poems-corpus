def get_wake_on_network():
    '''
    Displays whether 'wake on network' is on or off if supported

    :return: A string value representing the "wake on network" settings
    :rtype: string

    CLI Example:

    .. code-block:: bash

        salt '*' power.get_wake_on_network
    '''
    ret = salt.utils.mac_utils.execute_return_result(
        'systemsetup -getwakeonnetworkaccess')
    return salt.utils.mac_utils.validate_enabled(
        salt.utils.mac_utils.parse_return(ret)) == 'on'