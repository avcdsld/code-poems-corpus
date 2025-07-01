def create_summary_metadata(display_name, description):
  """Create a `summary_pb2.SummaryMetadata` proto for image plugin data.

  Returns:
    A `summary_pb2.SummaryMetadata` protobuf object.
  """
  content = plugin_data_pb2.ImagePluginData(version=PROTO_VERSION)
  metadata = summary_pb2.SummaryMetadata(
      display_name=display_name,
      summary_description=description,
      plugin_data=summary_pb2.SummaryMetadata.PluginData(
          plugin_name=PLUGIN_NAME,
          content=content.SerializeToString()))
  return metadata