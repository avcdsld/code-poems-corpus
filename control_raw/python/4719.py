def transformer_nat_big():
  """Set of hyperparameters."""
  hparams = transformer_nat_small()
  hparams.batch_size = 2048
  hparams.hidden_size = 1024
  hparams.filter_size = 4096
  hparams.num_hidden_layers = 6
  hparams.num_heads = 16
  hparams.layer_prepostprocess_dropout = 0.3
  return hparams