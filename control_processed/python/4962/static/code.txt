def infer(self, ob):
    """Add new observation to frame stack and infer policy.

    Args:
      ob: array of shape (height, width, channels)

    Returns:
      logits and vf.
    """
    self._add_to_stack(ob)
    logits, vf = self.infer_from_frame_stack(self._frame_stack)
    return logits, vf