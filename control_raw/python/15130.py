def set_input(self, X_batch=None):
    """
    Preprocessing the inputs before calling session.run()

    :param X_batch: A dictionary of inputs to the first sub-graph
    :return: A tuple, `(fetches, fd)`, with `fetches` being a list of
             Tensors to be fetches and `fd` the feed dictionary.
    """
    inputs = self.inputs
    outputs = self.outputs

    # data for first gpu
    fd = {}
    if X_batch is not None:
      self.next_vals[0] = OrderedDict()
      for i, vname in enumerate(self.inputs[0]):
        if vname in X_batch:
          self.next_vals[0][vname] = X_batch[vname]
        else:
          self.next_vals[0][vname] = None
    else:
      self.next_vals[0] = None

    # Set `feed_dict` for each GPU. If there is something to run for that
    # GPU, collect outputs to be fetched.
    fetches = []
    self.active_gpus = []
    for i in range(len(outputs)):
      if self.next_vals[i] is None:
        self.active_gpus += [False]
        continue
      self.active_gpus += [True]
      for k in inputs[i]:
        if self.next_vals[i][k] is not None:
          fd[inputs[i][k]] = self.next_vals[i][k]
      for k, v in outputs[i].iteritems():
        fetches += [v]

    fd.update(self.feed_dict)

    return fetches, fd