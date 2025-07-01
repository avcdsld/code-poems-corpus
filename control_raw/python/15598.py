def _string_hash(s):
    """String hash (djb2) with consistency between py2/py3 and persistency between runs (unlike `hash`)."""
    h = 5381
    for c in s:
        h = h * 33 + ord(c)
    return h