def change_last_time_step(self, **replace_time_step_kwargs):
    """Replace the last time-steps with the given kwargs."""

    # Pre-conditions: self._time_steps shouldn't be empty.
    assert self._time_steps
    self._time_steps[-1] = self._time_steps[-1].replace(
        **replace_time_step_kwargs)