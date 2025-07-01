def LogSoftmax(x, params, axis=-1, **kwargs):
  """Apply log softmax to x: log-normalize along the given axis."""
  del params, kwargs
  return x - backend.logsumexp(x, axis, keepdims=True)