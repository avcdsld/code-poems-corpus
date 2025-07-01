def _read(obj):
    """Try to read from a url, file or string.

    Parameters
    ----------
    obj : str, unicode, or file-like

    Returns
    -------
    raw_text : str
    """
    if _is_url(obj):
        with urlopen(obj) as url:
            text = url.read()
    elif hasattr(obj, 'read'):
        text = obj.read()
    elif isinstance(obj, (str, bytes)):
        text = obj
        try:
            if os.path.isfile(text):
                with open(text, 'rb') as f:
                    return f.read()
        except (TypeError, ValueError):
            pass
    else:
        raise TypeError("Cannot read object of type %r" % type(obj).__name__)
    return text