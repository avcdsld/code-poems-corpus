def AddExtensionDescriptor(self, extension):
    """Adds a FieldDescriptor describing an extension to the pool.

    Args:
      extension: A FieldDescriptor.

    Raises:
      AssertionError: when another extension with the same number extends the
        same message.
      TypeError: when the specified extension is not a
        descriptor.FieldDescriptor.
    """
    if not (isinstance(extension, descriptor.FieldDescriptor) and
            extension.is_extension):
      raise TypeError('Expected an extension descriptor.')

    if extension.extension_scope is None:
      self._toplevel_extensions[extension.full_name] = extension

    try:
      existing_desc = self._extensions_by_number[
          extension.containing_type][extension.number]
    except KeyError:
      pass
    else:
      if extension is not existing_desc:
        raise AssertionError(
            'Extensions "%s" and "%s" both try to extend message type "%s" '
            'with field number %d.' %
            (extension.full_name, existing_desc.full_name,
             extension.containing_type.full_name, extension.number))

    self._extensions_by_number[extension.containing_type][
        extension.number] = extension
    self._extensions_by_name[extension.containing_type][
        extension.full_name] = extension

    # Also register MessageSet extensions with the type name.
    if _IsMessageSetExtension(extension):
      self._extensions_by_name[extension.containing_type][
          extension.message_type.full_name] = extension