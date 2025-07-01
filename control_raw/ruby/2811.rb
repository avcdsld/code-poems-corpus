def append(events, stream_name: GLOBAL_STREAM, expected_version: :any)
      serialized_events = serialize_events(enrich_events_metadata(events))
      append_to_stream_serialized_events(serialized_events, stream_name: stream_name, expected_version: expected_version)
      self
    end