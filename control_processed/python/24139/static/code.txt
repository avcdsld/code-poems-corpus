def _get_account_policy(name):
    '''
    Get the entire accountPolicy and return it as a dictionary. For use by this
    module only

    :param str name: The user name

    :return: a dictionary containing all values for the accountPolicy
    :rtype: dict

    :raises: CommandExecutionError on user not found or any other unknown error
    '''

    cmd = 'pwpolicy -u {0} -getpolicy'.format(name)
    try:
        ret = salt.utils.mac_utils.execute_return_result(cmd)
    except CommandExecutionError as exc:
        if 'Error: user <{0}> not found'.format(name) in exc.strerror:
            raise CommandExecutionError('User not found: {0}'.format(name))
        raise CommandExecutionError('Unknown error: {0}'.format(exc.strerror))

    try:
        policy_list = ret.split('\n')[1].split(' ')
        policy_dict = {}
        for policy in policy_list:
            if '=' in policy:
                key, value = policy.split('=')
                policy_dict[key] = value
        return policy_dict
    except IndexError:
        return {}