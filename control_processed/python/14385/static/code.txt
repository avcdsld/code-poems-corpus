def _pb_timestamp_to_datetime(timestamp_pb):
    """Convert a Timestamp protobuf to a datetime object.

    :type timestamp_pb: :class:`google.protobuf.timestamp_pb2.Timestamp`
    :param timestamp_pb: A Google returned timestamp protobuf.

    :rtype: :class:`datetime.datetime`
    :returns: A UTC datetime object converted from a protobuf timestamp.
    """
    return _EPOCH + datetime.timedelta(
        seconds=timestamp_pb.seconds, microseconds=(timestamp_pb.nanos / 1000.0)
    )