def _dmi_cast(key, val, clean=True):
    '''
    Simple caster thingy for trying to fish out at least ints & lists from strings
    '''
    if clean and not _dmi_isclean(key, val):
        return
    elif not re.match(r'serial|part|asset|product', key, flags=re.IGNORECASE):
        if ',' in val:
            val = [el.strip() for el in val.split(',')]
        else:
            try:
                val = int(val)
            except Exception:
                pass

    return val