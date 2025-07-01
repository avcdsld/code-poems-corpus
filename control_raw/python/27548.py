def _read_dict(cp, dictionary):
    '''
    Cribbed from python3's ConfigParser.read_dict function.
    '''
    for section, keys in dictionary.items():
        section = six.text_type(section)

        if _is_defaultsect(section):
            if six.PY2:
                section = configparser.DEFAULTSECT
        else:
            cp.add_section(section)

        for key, value in keys.items():
            key = cp.optionxform(six.text_type(key))
            if value is not None:
                value = six.text_type(value)
            cp.set(section, key, value)