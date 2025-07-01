def create_summary_metadata(display_name, description, num_thresholds):
  """Create a `summary_pb2.SummaryMetadata` proto for pr_curves plugin data.

  Arguments:
    display_name: The display name used in TensorBoard.
    description: The description to show in TensorBoard.
    num_thresholds: The number of thresholds to use for PR curves.

  Returns:
    A `summary_pb2.SummaryMetadata` protobuf object.
  """
  pr_curve_plugin_data = plugin_data_pb2.PrCurvePluginData(
      version=PROTO_VERSION, num_thresholds=num_thresholds)
  content = pr_curve_plugin_data.SerializeToString()
  return summary_pb2.SummaryMetadata(
      display_name=display_name,
      summary_description=description,
      plugin_data=summary_pb2.SummaryMetadata.PluginData(
          plugin_name=PLUGIN_NAME,
          content=content))