def set_shape(self, shape):
    """Update the shape."""
    channels = shape[-1]
    acceptable_channels = ACCEPTABLE_CHANNELS[self._encoding_format]
    if channels not in acceptable_channels:
      raise ValueError('Acceptable `channels` for %s: %s (was %s)' % (
          self._encoding_format, acceptable_channels, channels))
    self._shape = tuple(shape)