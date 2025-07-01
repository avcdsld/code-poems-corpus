def _find_metric_value(session_or_group, metric_name):
  """Returns the metric_value for a given metric in a session or session group.

  Args:
    session_or_group: A Session protobuffer or SessionGroup protobuffer.
    metric_name: A MetricName protobuffer. The metric to search for.
  Returns:
    A MetricValue protobuffer representing the value of the given metric or
    None if no such metric was found in session_or_group.
  """
  # Note: We can speed this up by converting the metric_values field
  # to a dictionary on initialization, to avoid a linear search here. We'll
  # need to wrap the SessionGroup and Session protos in a python object for
  # that.
  for metric_value in session_or_group.metric_values:
    if (metric_value.name.tag == metric_name.tag and
        metric_value.name.group == metric_name.group):
      return metric_value