def get_profile(profile, caller, runner):
    '''
    Get profile.

    :param profile:
    :return:
    '''
    profiles = profile.split(',')
    data = {}
    for profile in profiles:
        if os.path.basename(profile) == profile:
            profile = profile.split('.')[0]  # Trim extension if someone added it
            profile_path = os.path.join(os.path.dirname(__file__), 'profiles', profile + '.yml')
        else:
            profile_path = profile
        if os.path.exists(profile_path):
            try:
                rendered_template = _render_profile(profile_path, caller, runner)
                line = '-' * 80
                log.debug('\n%s\n%s\n%s\n', line, rendered_template, line)
                data.update(yaml.load(rendered_template))
            except Exception as ex:
                log.debug(ex, exc_info=True)
                raise salt.exceptions.SaltException('Rendering profile failed: {}'.format(ex))
        else:
            raise salt.exceptions.SaltException('Profile "{}" is not found.'.format(profile))

    return data