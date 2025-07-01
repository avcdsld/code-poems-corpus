def profile_list(default_only=False):
    '''
    List all available profiles

    default_only : boolean
        return only default profile

    CLI Example:

    .. code-block:: bash

        salt '*' rbac.profile_list
    '''
    profiles = {}
    default_profiles = ['All']

    ## lookup default profile(s)
    with salt.utils.files.fopen('/etc/security/policy.conf', 'r') as policy_conf:
        for policy in policy_conf:
            policy = salt.utils.stringutils.to_unicode(policy)
            policy = policy.split('=')
            if policy[0].strip() == 'PROFS_GRANTED':
                default_profiles.extend(policy[1].strip().split(','))

    ## read prof_attr file (profname:res1:res2:desc:attr)
    with salt.utils.files.fopen('/etc/security/prof_attr', 'r') as prof_attr:
        for profile in prof_attr:
            profile = salt.utils.stringutils.to_unicode(profile)
            profile = profile.split(':')

            # skip comments and non complaint lines
            if len(profile) != 5:
                continue

            # add profile info to dict
            profiles[profile[0]] = profile[3]

    ## filtered profiles
    if default_only:
        for p in [p for p in profiles if p not in default_profiles]:
            del profiles[p]

    return profiles