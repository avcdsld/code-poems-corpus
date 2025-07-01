def _context_string_to_dict(context):
    '''
    .. versionadded:: 2017.7.0

    Converts an SELinux file context from string to dict.
    '''
    if not re.match('[^:]+:[^:]+:[^:]+:[^:]+$', context):
        raise SaltInvocationError('Invalid SELinux context string: {0}. ' +
                                  'Expected "sel_user:sel_role:sel_type:sel_level"')
    context_list = context.split(':', 3)
    ret = {}
    for index, value in enumerate(['sel_user', 'sel_role', 'sel_type', 'sel_level']):
        ret[value] = context_list[index]
    return ret