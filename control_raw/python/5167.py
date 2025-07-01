def decode(self, ids, strip_extraneous=False):
    """Transform a sequence of int ids into a human-readable string.

    EOS is not expected in ids.

    Args:
      ids: list of integers to be converted.
      strip_extraneous: bool, whether to strip off extraneous tokens
        (EOS and PAD).

    Returns:
      s: human-readable string.
    """
    if strip_extraneous:
      ids = strip_ids(ids, list(range(self._num_reserved_ids or 0)))
    return " ".join(self.decode_list(ids))