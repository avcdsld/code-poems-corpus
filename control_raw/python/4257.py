def xmoe2_v1_l4k():
  """With sequence length 4096."""
  hparams = xmoe2_v1()
  hparams.batch_size = 32
  hparams.max_length = 4096
  hparams.split_to_length = 4096
  hparams.reshape_logits_hack = True
  return hparams