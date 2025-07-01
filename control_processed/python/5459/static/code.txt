def lmx_h4k_f16k():
  """HParams for training languagemodel_lm1b32k_packed.  1470M Params."""
  hparams = lmx_base()
  hparams.hidden_size = 4096
  hparams.filter_size = 16384
  hparams.batch_size = 1024
  hparams.weight_dtype = "bfloat16"
  return hparams