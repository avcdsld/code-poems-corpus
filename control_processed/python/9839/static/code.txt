def format_header_param(name, value):
    """
    Helper function to format and quote a single header parameter.

    Particularly useful for header parameters which might contain
    non-ASCII values, like file names. This follows RFC 2231, as
    suggested by RFC 2388 Section 4.4.

    :param name:
        The name of the parameter, a string expected to be ASCII only.
    :param value:
        The value of the parameter, provided as a unicode string.
    """
    if not any(ch in value for ch in '"\\\r\n'):
        result = '%s="%s"' % (name, value)
        try:
            result.encode('ascii')
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
        else:
            return result
    if not six.PY3 and isinstance(value, six.text_type):  # Python 2:
        value = value.encode('utf-8')
    value = email.utils.encode_rfc2231(value, 'utf-8')
    value = '%s*=%s' % (name, value)
    return value