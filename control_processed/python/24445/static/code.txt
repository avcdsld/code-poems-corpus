def _str_elem(config, key):

    '''
    Re-adds the value of a specific key in the dict, only in case of valid str value.
    '''

    _value = config.pop(key, '')
    if _valid_str(_value):
        config[key] = _value