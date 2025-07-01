def list_registered_stateful_ops_without_inputs():
  """Returns set of registered stateful ops that do not expect inputs.

  This list is used to identify the ops to be included in the state-graph and
  that are subsequently fed into the apply-graphs.

  Returns:
    A set of strings.
  """
  return set([
      name
      for name, op in op_def_registry.get_registered_ops().items()
      if op.is_stateful and not op.input_arg
  ])