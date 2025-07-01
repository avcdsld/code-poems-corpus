def strtobool(val):
    """
    This function was borrowed from distutils.utils. While distutils
    is part of stdlib, it feels odd to use distutils in main application code.

    The function was modified to walk its talk and actually return bool
    and not int.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif val in ("n", "no", "f", "false", "off", "0"):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))