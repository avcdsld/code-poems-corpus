def get_profiles(config):
    '''
    Get available profiles.

    :return:
    '''
    profiles = []
    for profile_name in os.listdir(os.path.join(os.path.dirname(__file__), 'profiles')):
        if profile_name.endswith('.yml'):
            profiles.append(profile_name.split('.')[0])

    return sorted(profiles)