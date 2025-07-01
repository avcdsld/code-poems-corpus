def _normalize_args(args):
    '''
    Return args as a list of strings
    '''
    if isinstance(args, six.string_types):
        return shlex.split(args)

    if isinstance(args, (tuple, list)):
        return [six.text_type(arg) for arg in args]
    else:
        return [six.text_type(args)]