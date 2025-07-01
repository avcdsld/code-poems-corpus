def find_signature_inputs_from_multivalued_ops(inputs):
  """Returns error message for module inputs from ops with multiple outputs."""
  dense_inputs = []  # List of (str, Tensor), with SparseTensors decomposed.
  for name, tensor in sorted(inputs.items()):
    if isinstance(tensor, tf.SparseTensor):
      dense_inputs.extend(("%s.%s" % (name, attr), getattr(tensor, attr))
                          for attr in ("indices", "values", "dense_shape"))
    else:
      dense_inputs.append((name, tensor))
  warnings = [(name, tensor.name) for name, tensor in dense_inputs
              if len(tensor.op.outputs) != 1]
  if warnings:
    return (
        "WARNING: The inputs declared in hub.add_signature() should be tensors "
        "from ops with a single output, or else uses of tf.colocate_with() on "
        "that op can trigger fatal errors when the module is applied and "
        "colocation constraints have to be rewritten.\nAffected inputs: %s" %
        ", ".join("%s='%s'" % pair for pair in warnings))
  return None