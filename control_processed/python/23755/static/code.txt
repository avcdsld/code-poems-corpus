def __space_delimited_list(value):
    '''validate that a value contains one or more space-delimited values'''
    if isinstance(value, six.string_types):
        value = value.strip().split()

    if hasattr(value, '__iter__') and value != []:
        return (True, value, 'space-delimited string')
    else:
        return (False, value, '{0} is not a valid space-delimited value.\n'.format(value))