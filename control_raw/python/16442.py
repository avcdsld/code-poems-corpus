def _MergeField(self, tokenizer, message):
    """Merges a single protocol message field into a message.

    Args:
      tokenizer: A tokenizer to parse the field name and values.
      message: A protocol message to record the data.

    Raises:
      ParseError: In case of text parsing problems.
    """
    message_descriptor = message.DESCRIPTOR
    if (hasattr(message_descriptor, 'syntax') and
        message_descriptor.syntax == 'proto3'):
      # Proto3 doesn't represent presence so we can't test if multiple
      # scalars have occurred.  We have to allow them.
      self._allow_multiple_scalars = True
    if tokenizer.TryConsume('['):
      name = [tokenizer.ConsumeIdentifier()]
      while tokenizer.TryConsume('.'):
        name.append(tokenizer.ConsumeIdentifier())
      name = '.'.join(name)

      if not message_descriptor.is_extendable:
        raise tokenizer.ParseErrorPreviousToken(
            'Message type "%s" does not have extensions.' %
            message_descriptor.full_name)
      # pylint: disable=protected-access
      field = message.Extensions._FindExtensionByName(name)
      # pylint: enable=protected-access
      if not field:
        if self.allow_unknown_extension:
          field = None
        else:
          raise tokenizer.ParseErrorPreviousToken(
              'Extension "%s" not registered.' % name)
      elif message_descriptor != field.containing_type:
        raise tokenizer.ParseErrorPreviousToken(
            'Extension "%s" does not extend message type "%s".' %
            (name, message_descriptor.full_name))

      tokenizer.Consume(']')

    else:
      name = tokenizer.ConsumeIdentifierOrNumber()
      if self.allow_field_number and name.isdigit():
        number = ParseInteger(name, True, True)
        field = message_descriptor.fields_by_number.get(number, None)
        if not field and message_descriptor.is_extendable:
          field = message.Extensions._FindExtensionByNumber(number)
      else:
        field = message_descriptor.fields_by_name.get(name, None)

        # Group names are expected to be capitalized as they appear in the
        # .proto file, which actually matches their type names, not their field
        # names.
        if not field:
          field = message_descriptor.fields_by_name.get(name.lower(), None)
          if field and field.type != descriptor.FieldDescriptor.TYPE_GROUP:
            field = None

        if (field and field.type == descriptor.FieldDescriptor.TYPE_GROUP and
            field.message_type.name != name):
          field = None

      if not field:
        raise tokenizer.ParseErrorPreviousToken(
            'Message type "%s" has no field named "%s".' %
            (message_descriptor.full_name, name))

    if field:
      if not self._allow_multiple_scalars and field.containing_oneof:
        # Check if there's a different field set in this oneof.
        # Note that we ignore the case if the same field was set before, and we
        # apply _allow_multiple_scalars to non-scalar fields as well.
        which_oneof = message.WhichOneof(field.containing_oneof.name)
        if which_oneof is not None and which_oneof != field.name:
          raise tokenizer.ParseErrorPreviousToken(
              'Field "%s" is specified along with field "%s", another member '
              'of oneof "%s" for message type "%s".' %
              (field.name, which_oneof, field.containing_oneof.name,
               message_descriptor.full_name))

      if field.cpp_type == descriptor.FieldDescriptor.CPPTYPE_MESSAGE:
        tokenizer.TryConsume(':')
        merger = self._MergeMessageField
      else:
        tokenizer.Consume(':')
        merger = self._MergeScalarField

      if (field.label == descriptor.FieldDescriptor.LABEL_REPEATED and
          tokenizer.TryConsume('[')):
        # Short repeated format, e.g. "foo: [1, 2, 3]"
        while True:
          merger(tokenizer, message, field)
          if tokenizer.TryConsume(']'):
            break
          tokenizer.Consume(',')

      else:
        merger(tokenizer, message, field)

    else:  # Proto field is unknown.
      assert self.allow_unknown_extension
      _SkipFieldContents(tokenizer)

    # For historical reasons, fields may optionally be separated by commas or
    # semicolons.
    if not tokenizer.TryConsume(','):
      tokenizer.TryConsume(';')