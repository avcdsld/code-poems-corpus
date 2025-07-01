def pprint_thing(thing, _nest_lvl=0, escape_chars=None, default_escapes=False,
                 quote_strings=False, max_seq_items=None):
    """
    This function is the sanctioned way of converting objects
    to a unicode representation.

    properly handles nested sequences containing unicode strings
    (unicode(object) does not)

    Parameters
    ----------
    thing : anything to be formatted
    _nest_lvl : internal use only. pprint_thing() is mutually-recursive
        with pprint_sequence, this argument is used to keep track of the
        current nesting level, and limit it.
    escape_chars : list or dict, optional
        Characters to escape. If a dict is passed the values are the
        replacements
    default_escapes : bool, default False
        Whether the input escape characters replaces or adds to the defaults
    max_seq_items : False, int, default None
        Pass thru to other pretty printers to limit sequence printing

    Returns
    -------
    result - unicode str

    """

    def as_escaped_unicode(thing, escape_chars=escape_chars):
        # Unicode is fine, else we try to decode using utf-8 and 'replace'
        # if that's not it either, we have no way of knowing and the user
        # should deal with it himself.

        try:
            result = str(thing)  # we should try this first
        except UnicodeDecodeError:
            # either utf-8 or we replace errors
            result = str(thing).decode('utf-8', "replace")

        translate = {'\t': r'\t', '\n': r'\n', '\r': r'\r', }
        if isinstance(escape_chars, dict):
            if default_escapes:
                translate.update(escape_chars)
            else:
                translate = escape_chars
            escape_chars = list(escape_chars.keys())
        else:
            escape_chars = escape_chars or tuple()
        for c in escape_chars:
            result = result.replace(c, translate[c])

        return str(result)

    if hasattr(thing, '__next__'):
        return str(thing)
    elif (isinstance(thing, dict) and
          _nest_lvl < get_option("display.pprint_nest_depth")):
        result = _pprint_dict(thing, _nest_lvl, quote_strings=True,
                              max_seq_items=max_seq_items)
    elif (is_sequence(thing) and
          _nest_lvl < get_option("display.pprint_nest_depth")):
        result = _pprint_seq(thing, _nest_lvl, escape_chars=escape_chars,
                             quote_strings=quote_strings,
                             max_seq_items=max_seq_items)
    elif isinstance(thing, str) and quote_strings:
        result = "'{thing}'".format(thing=as_escaped_unicode(thing))
    else:
        result = as_escaped_unicode(thing)

    return str(result)