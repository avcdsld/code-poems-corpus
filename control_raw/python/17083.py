def _ConvertInteger(value):
  """Convert an integer.

  Args:
    value: A scalar value to convert.

  Returns:
    The integer value.

  Raises:
    ParseError: If an integer couldn't be consumed.
  """
  if isinstance(value, float) and not value.is_integer():
    raise ParseError('Couldn\'t parse integer: {0}.'.format(value))

  if isinstance(value, six.text_type) and value.find(' ') != -1:
    raise ParseError('Couldn\'t parse integer: "{0}".'.format(value))

  return int(value)