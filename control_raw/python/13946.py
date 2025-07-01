def entity_to_protobuf(entity):
    """Converts an entity into a protobuf.

    :type entity: :class:`google.cloud.datastore.entity.Entity`
    :param entity: The entity to be turned into a protobuf.

    :rtype: :class:`.entity_pb2.Entity`
    :returns: The protobuf representing the entity.
    """
    entity_pb = entity_pb2.Entity()
    if entity.key is not None:
        key_pb = entity.key.to_protobuf()
        entity_pb.key.CopyFrom(key_pb)

    for name, value in entity.items():
        value_is_list = isinstance(value, list)

        value_pb = _new_value_pb(entity_pb, name)
        # Set the appropriate value.
        _set_protobuf_value(value_pb, value)

        # Add index information to protobuf.
        if name in entity.exclude_from_indexes:
            if not value_is_list:
                value_pb.exclude_from_indexes = True

            for sub_value in value_pb.array_value.values:
                sub_value.exclude_from_indexes = True

        # Add meaning information to protobuf.
        _set_pb_meaning_from_entity(
            entity, name, value, value_pb, is_list=value_is_list
        )

    return entity_pb