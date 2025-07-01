def get_field_to_observations_map(generator, query_for_tag=''):
  """Return a field to `Observations` dict for the event generator.

  Args:
    generator: A generator over event protos.
    query_for_tag: A string that if specified, only create observations for
      events with this tag name.

  Returns:
    A dict mapping keys in `TRACKED_FIELDS` to an `Observation` list.
  """

  def increment(stat, event, tag=''):
    assert stat in TRACKED_FIELDS
    field_to_obs[stat].append(Observation(step=event.step,
                                          wall_time=event.wall_time,
                                          tag=tag)._asdict())

  field_to_obs = dict([(t, []) for t in TRACKED_FIELDS])

  for event in generator:
    ## Process the event
    if event.HasField('graph_def') and (not query_for_tag):
      increment('graph', event)
    if event.HasField('session_log') and (not query_for_tag):
      status = event.session_log.status
      if status == event_pb2.SessionLog.START:
        increment('sessionlog:start', event)
      elif status == event_pb2.SessionLog.STOP:
        increment('sessionlog:stop', event)
      elif status == event_pb2.SessionLog.CHECKPOINT:
        increment('sessionlog:checkpoint', event)
    elif event.HasField('summary'):
      for value in event.summary.value:
        if query_for_tag and value.tag != query_for_tag:
          continue

        for proto_name, display_name in SUMMARY_TYPE_TO_FIELD.items():
          if value.HasField(proto_name):
            increment(display_name, event, value.tag)
  return field_to_obs