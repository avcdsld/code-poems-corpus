def markdown_to_safe_html(markdown_string):
  """Convert Markdown to HTML that's safe to splice into the DOM.

  Arguments:
    markdown_string: A Unicode string or UTF-8--encoded bytestring
      containing Markdown source. Markdown tables are supported.

  Returns:
    A string containing safe HTML.
  """
  warning = ''
  # Convert to utf-8 whenever we have a binary input.
  if isinstance(markdown_string, six.binary_type):
    markdown_string_decoded = markdown_string.decode('utf-8')
    # Remove null bytes and warn if there were any, since it probably means
    # we were given a bad encoding.
    markdown_string = markdown_string_decoded.replace(u'\x00', u'')
    num_null_bytes = len(markdown_string_decoded) - len(markdown_string)
    if num_null_bytes:
      warning = ('<!-- WARNING: discarded %d null bytes in markdown string '
                 'after UTF-8 decoding -->\n') % num_null_bytes

  string_html = markdown.markdown(
      markdown_string, extensions=['markdown.extensions.tables'])
  string_sanitized = bleach.clean(
      string_html, tags=_ALLOWED_TAGS, attributes=_ALLOWED_ATTRIBUTES)
  return warning + string_sanitized