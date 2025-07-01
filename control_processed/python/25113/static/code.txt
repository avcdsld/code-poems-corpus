def translate_device_rates(val, numeric_rate=True):
    '''
    CLI input is a list of PATH:RATE pairs, but the API expects a list of
    dictionaries in the format [{'Path': path, 'Rate': rate}]
    '''
    val = map_vals(val, 'Path', 'Rate')
    for idx in range(len(val)):
        try:
            is_abs = os.path.isabs(val[idx]['Path'])
        except AttributeError:
            is_abs = False
        if not is_abs:
            raise SaltInvocationError(
                'Path \'{Path}\' is not absolute'.format(**val[idx])
            )

        # Attempt to convert to an integer. Will fail if rate was specified as
        # a shorthand (e.g. 1mb), this is OK as we will check to make sure the
        # value is an integer below if that is what is required.
        try:
            val[idx]['Rate'] = int(val[idx]['Rate'])
        except (TypeError, ValueError):
            pass

        if numeric_rate:
            try:
                val[idx]['Rate'] = int(val[idx]['Rate'])
            except ValueError:
                raise SaltInvocationError(
                    'Rate \'{Rate}\' for path \'{Path}\' is '
                    'non-numeric'.format(**val[idx])
                )
    return val