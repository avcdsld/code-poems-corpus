def symbol_targets_bottom(x, model_hparams, vocab_size):
  """Bottom transformation for target symbols."""
  if (model_hparams.shared_embedding_and_softmax_weights or
      model_hparams.get("shared_embedding")):
    try:
      return _symbol_bottom_simple(
          x, model_hparams, vocab_size, "shared", reuse=True)
    except ValueError:
      # perhaps there were no inputs, and this is a new variable.
      return _symbol_bottom_simple(
          x, model_hparams, vocab_size, "shared", reuse=None)
  else:
    return _symbol_bottom_simple(
        x, model_hparams, vocab_size, "target_emb", reuse=None)