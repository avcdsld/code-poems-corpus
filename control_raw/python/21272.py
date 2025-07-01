def _safe_copy_proto_list_values(dst_proto_list, src_proto_list, get_key):
  """Safely merge values from `src_proto_list` into `dst_proto_list`.

  Each element in `dst_proto_list` must be mapped by `get_key` to a key
  value that is unique within that list; likewise for `src_proto_list`.
  If an element of `src_proto_list` has the same key as an existing
  element in `dst_proto_list`, then the elements must also be equal.

  Args:
    dst_proto_list: A `RepeatedCompositeContainer` or
      `RepeatedScalarContainer` into which values should be copied.
    src_proto_list: A container holding the same kind of values as in
      `dst_proto_list` from which values should be copied.
    get_key: A function that takes an element of `dst_proto_list` or
      `src_proto_list` and returns a key, such that if two elements have
      the same key then it is required that they be deep-equal. For
      instance, if `dst_proto_list` is a list of nodes, then `get_key`
      might be `lambda node: node.name` to indicate that if two nodes
      have the same name then they must be the same node. All keys must
      be hashable.

  Raises:
    _ProtoListDuplicateKeyError: A proto_list contains items with duplicate
      keys.
    _SameKeyDiffContentError: An item with the same key has different contents.
  """

  def _assert_proto_container_unique_keys(proto_list, get_key):
    """Asserts proto_list to only contains unique keys.

    Args:
      proto_list: A `RepeatedCompositeContainer` or `RepeatedScalarContainer`.
      get_key: A function that takes an element of `proto_list` and returns a
        hashable key.

    Raises:
      _ProtoListDuplicateKeyError: A proto_list contains items with duplicate
        keys.
    """
    keys = set()
    for item in proto_list:
      key = get_key(item)
      if key in keys:
        raise _ProtoListDuplicateKeyError(key)
      keys.add(key)

  _assert_proto_container_unique_keys(dst_proto_list, get_key)
  _assert_proto_container_unique_keys(src_proto_list, get_key)

  key_to_proto = {}
  for proto in dst_proto_list:
    key = get_key(proto)
    key_to_proto[key] = proto

  for proto in src_proto_list:
    key = get_key(proto)
    if key in key_to_proto:
      if proto != key_to_proto.get(key):
        raise _SameKeyDiffContentError(key)
    else:
      dst_proto_list.add().CopyFrom(proto)