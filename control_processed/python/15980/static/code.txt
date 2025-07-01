def ParseMessage(descriptor, byte_str):
  """Generate a new Message instance from this Descriptor and a byte string.

  Args:
    descriptor: Protobuf Descriptor object
    byte_str: Serialized protocol buffer byte string

  Returns:
    Newly created protobuf Message object.
  """
  result_class = MakeClass(descriptor)
  new_msg = result_class()
  new_msg.ParseFromString(byte_str)
  return new_msg