def Parse(text,
          message,
          allow_unknown_extension=False,
          allow_field_number=False,
          descriptor_pool=None):
  """Parses a text representation of a protocol message into a message.

  Args:
    text: Message text representation.
    message: A protocol buffer message to merge into.
    allow_unknown_extension: if True, skip over missing extensions and keep
      parsing
    allow_field_number: if True, both field number and field name are allowed.
    descriptor_pool: A DescriptorPool used to resolve Any types.

  Returns:
    The same message passed as argument.

  Raises:
    ParseError: On text parsing problems.
  """
  if not isinstance(text, str):
    text = text.decode('utf-8')
  return ParseLines(text.split('\n'),
                    message,
                    allow_unknown_extension,
                    allow_field_number,
                    descriptor_pool=descriptor_pool)