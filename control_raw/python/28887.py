def enforce_types(key, val):
    '''
    Force params to be strings unless they should remain a different type
    '''
    non_string_params = {
        'ssl_verify': bool,
        'insecure_auth': bool,
        'disable_saltenv_mapping': bool,
        'env_whitelist': 'stringlist',
        'env_blacklist': 'stringlist',
        'saltenv_whitelist': 'stringlist',
        'saltenv_blacklist': 'stringlist',
        'refspecs': 'stringlist',
        'ref_types': 'stringlist',
        'update_interval': int,
    }

    def _find_global(key):
        for item in non_string_params:
            try:
                if key.endswith('_' + item):
                    ret = item
                    break
            except TypeError:
                if key.endswith('_' + six.text_type(item)):
                    ret = item
                    break
        else:
            ret = None
        return ret

    if key not in non_string_params:
        key = _find_global(key)
        if key is None:
            return six.text_type(val)

    expected = non_string_params[key]
    if expected == 'stringlist':
        if not isinstance(val, (six.string_types, list)):
            val = six.text_type(val)
        if isinstance(val, six.string_types):
            return [x.strip() for x in val.split(',')]
        return [six.text_type(x) for x in val]
    else:
        try:
            return expected(val)
        except Exception as exc:
            log.error(
                'Failed to enforce type for key=%s with val=%s, falling back '
                'to a string', key, val
            )
            return six.text_type(val)