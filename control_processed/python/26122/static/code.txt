def enabled(name='allprofiles'):
    '''
    Enable all the firewall profiles (Windows only)

    Args:
        profile (Optional[str]): The name of the profile to enable. Default is
            ``allprofiles``. Valid options are:

            - allprofiles
            - domainprofile
            - privateprofile
            - publicprofile

    Example:

    .. code-block:: yaml

        # To enable the domain profile
        enable_domain:
          win_firewall.enabled:
            - name: domainprofile

        # To enable all profiles
        enable_all:
          win_firewall.enabled:
            - name: allprofiles
    '''
    ret = {'name': name,
           'result': True,
           'changes': {},
           'comment': ''}

    profile_map = {'domainprofile': 'Domain',
                   'privateprofile': 'Private',
                   'publicprofile': 'Public',
                   'allprofiles': 'All'}

    # Make sure the profile name is valid
    if name not in profile_map:
        raise SaltInvocationError('Invalid profile name: {0}'.format(name))

    current_config = __salt__['firewall.get_config']()
    if name != 'allprofiles' and profile_map[name] not in current_config:
        ret['result'] = False
        ret['comment'] = 'Profile {0} does not exist in firewall.get_config' \
                         ''.format(name)
        return ret

    for key in current_config:
        if not current_config[key]:
            if name == 'allprofiles' or key == profile_map[name]:
                ret['changes'][key] = 'enabled'

    if __opts__['test']:
        ret['result'] = not ret['changes'] or None
        ret['comment'] = ret['changes']
        ret['changes'] = {}
        return ret

    # Enable it
    if ret['changes']:
        try:
            ret['result'] = __salt__['firewall.enable'](name)
        except CommandExecutionError:
            ret['comment'] = 'Firewall Profile {0} could not be enabled' \
                             ''.format(profile_map[name])
    else:
        if name == 'allprofiles':
            msg = 'All the firewall profiles are enabled'
        else:
            msg = 'Firewall profile {0} is enabled'.format(name)
        ret['comment'] = msg

    return ret