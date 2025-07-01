def _parse_routes(iface, opts):
    '''
    Filters given options and outputs valid settings for
    the route settings file.
    '''
    # Normalize keys
    opts = dict((k.lower(), v) for (k, v) in six.iteritems(opts))
    result = {}
    if 'routes' not in opts:
        _raise_error_routes(iface, 'routes', 'List of routes')

    for opt in opts:
        result[opt] = opts[opt]

    return result