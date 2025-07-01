def MapDecoder(field_descriptor, new_default, is_message_map):
  """Returns a decoder for a map field."""

  key = field_descriptor
  tag_bytes = encoder.TagBytes(field_descriptor.number,
                               wire_format.WIRETYPE_LENGTH_DELIMITED)
  tag_len = len(tag_bytes)
  local_DecodeVarint = _DecodeVarint
  # Can't read _concrete_class yet; might not be initialized.
  message_type = field_descriptor.message_type

  def DecodeMap(buffer, pos, end, message, field_dict):
    submsg = message_type._concrete_class()
    value = field_dict.get(key)
    if value is None:
      value = field_dict.setdefault(key, new_default(message))
    while 1:
      # Read length.
      (size, pos) = local_DecodeVarint(buffer, pos)
      new_pos = pos + size
      if new_pos > end:
        raise _DecodeError('Truncated message.')
      # Read sub-message.
      submsg.Clear()
      if submsg._InternalParse(buffer, pos, new_pos) != new_pos:
        # The only reason _InternalParse would return early is if it
        # encountered an end-group tag.
        raise _DecodeError('Unexpected end-group tag.')

      if is_message_map:
        value[submsg.key].MergeFrom(submsg.value)
      else:
        value[submsg.key] = submsg.value

      # Predict that the next tag is another copy of the same repeated field.
      pos = new_pos + tag_len
      if buffer[new_pos:pos] != tag_bytes or new_pos == end:
        # Prediction failed.  Return.
        return new_pos

  return DecodeMap