def PluginTagToContent(self, plugin_name):
    """Returns a dict mapping tags to content specific to that plugin.

    Args:
      plugin_name: The name of the plugin for which to fetch plugin-specific
        content.

    Raises:
      KeyError: if the plugin name is not found.

    Returns:
      A dict mapping tags to plugin-specific content (which are always strings).
      Those strings are often serialized protos.
    """
    if plugin_name not in self._plugin_to_tag_to_content:
      raise KeyError('Plugin %r could not be found.' % plugin_name)
    with self._plugin_tag_locks[plugin_name]:
      # Return a snapshot to avoid concurrent mutation and iteration issues.
      return dict(self._plugin_to_tag_to_content[plugin_name])