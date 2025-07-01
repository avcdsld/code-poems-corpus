def normalize_locale(loc):
    '''
    Format a locale specifier according to the format returned by `locale -a`.
    '''
    comps = split_locale(loc)
    comps['territory'] = comps['territory'].upper()
    comps['codeset'] = comps['codeset'].lower().replace('-', '')
    comps['charmap'] = ''
    return join_locale(comps)