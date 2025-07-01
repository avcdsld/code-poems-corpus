def MethodCalled(self, mock_method):
    """Remove a method call from the group.

    If the method is not in the set, an UnexpectedMethodCallError will be
    raised.

    Args:
      mock_method: a mock method that should be equal to a method in the group.

    Returns:
      The mock method from the group

    Raises:
      UnexpectedMethodCallError if the mock_method was not in the group.
    """

    # Check to see if this method exists, and if so add it to the set of
    # called methods.

    for method in self._methods:
      if method == mock_method:
        self._methods_called.add(mock_method)
        # Always put this group back on top of the queue, because we don't know
        # when we are done.
        mock_method._call_queue.appendleft(self)
        return self, method

    if self.IsSatisfied():
      next_method = mock_method._PopNextMethod();
      return next_method, None
    else:
      raise UnexpectedMethodCallError(mock_method, self)