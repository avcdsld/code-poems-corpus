def _jit_predict_fun(model_predict, num_devices):
  """Use jit on model_predict if required."""
  def predict(x, params=(), rng=None):
    """Predict function jited and parallelized as requested."""
    # On one device, jit and run.
    if num_devices == 1:
      return backend.jit(model_predict)(x, params, rng=rng)

    # Multi-devices, pmap and run.
    @functools.partial(backend.pmap, axis_name="batch")
    def mapped_predict(x, params, rng):
      return model_predict(x, params, rng=rng)
    pred = mapped_predict(
        reshape_by_device(x, num_devices),
        params,
        jax_random.split(rng, num_devices))
    # Need to reduce the [device, per-device-batch, ...] tensors back to
    # a [batch, ...] tensor. The tensors may be nested.
    if not isinstance(x, (list, tuple)):  # Not nested.
      batch_size = x.shape[0]
      return np.reshape(pred, [batch_size] + list(pred.shape[2:]))
    batch_size = x[0].shape[0]
    return [np.reshape(p, [batch_size] + list(p.shape[2:])) for p in pred]

  return predict