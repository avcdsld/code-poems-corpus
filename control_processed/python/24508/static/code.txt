def _get_file_auth_config():
    '''
    Setup defaults and check configuration variables for auth backends
    '''

    config = {
        'filetype': 'text',
        'hashtype': 'plaintext',
        'field_separator': ':',
        'username_field': 1,
        'password_field': 2,
    }

    for opt in __opts__['external_auth'][__virtualname__]:
        if opt.startswith('^'):
            config[opt[1:]] = __opts__['external_auth'][__virtualname__][opt]

    if 'filename' not in config:
        log.error('salt.auth.file: An authentication file must be specified '
                  'via external_auth:file:^filename')
        return False

    if not os.path.exists(config['filename']):
        log.error('salt.auth.file: The configured external_auth:file:^filename (%s)'
                  'does not exist on the filesystem', config['filename'])
        return False

    config['username_field'] = int(config['username_field'])
    config['password_field'] = int(config['password_field'])

    return config