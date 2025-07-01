def targeted_dropout(inputs,
                     k,
                     keep_prob,
                     targeting_fn,
                     is_training,
                     do_prune=False):
  """Applies targeted dropout.

  Applies dropout at a rate of `1 - keep_prob` to only those elements of
  `inputs` marked by `targeting_fn`. See below and paper for more detail:

  "Targeted Dropout for Posthoc Pruning" Aidan N. Gomez, Ivan Zhang,
    Kevin Swersky, Yarin Gal, and Geoffrey E. Hinton.

  Args:
    inputs: Tensor, inputs to apply targeted dropout to.
    k: Scalar Tensor or python scalar, sets the number of elements to target in
      `inputs`. Must be within `[0, tf.shape(x)[-1]]` and compatible with
      second argument of `targeting_fn`.
    keep_prob: Scalar Tensor, passed as `tf.nn.dropout`'s `keep_prob` argument.
    targeting_fn: callable `fn(inputs, k) -> Boolean Tensor`, produces a
      boolean mask the same shape as `inputs` where True indicates an element
      will be dropped, and False not.
    is_training: bool, indicates whether currently training.
    do_prune: bool, indicates whether to prune the `k * (1 - keep_prob)`
      elements of `inputs` expected to be dropped each forwards pass.

  Returns:
    Tensor, same shape and dtype as `inputs`.
  """
  if not is_training and do_prune:
    k = tf.round(to_float(k) * to_float(1. - keep_prob))

  mask = targeting_fn(inputs, k)
  mask = tf.cast(mask, inputs.dtype)

  if is_training:
    return inputs * (1 - mask) + tf.nn.dropout(inputs, keep_prob) * mask
  elif do_prune:
    return inputs * (1 - mask)
  else:
    return inputs