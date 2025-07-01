def _indent(s, indent='  '):
    """Intent each line with indent"""
    if isinstance(s, six.string_types):
        return '\n'.join(('%s%s' % (indent, line) for line in s.splitlines()))
    return s