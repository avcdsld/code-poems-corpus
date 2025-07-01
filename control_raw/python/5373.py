def transformer_tall_pretrain_lm_tpu_adafactor_large():
  """Hparams for transformer on LM pretraining on TPU, large model."""
  hparams = transformer_tall_pretrain_lm_tpu_adafactor()
  hparams.hidden_size = 1024
  hparams.num_heads = 16
  hparams.filter_size = 32768  # max fitting in 16G memory is 49152, batch 2
  hparams.batch_size = 4
  hparams.multiproblem_mixing_schedule = "constant"
  # Task order: lm/en-de/en-fr/en-ro/de-en/fr-en/ro-en/cnndm/mnli/squad.
  hparams.multiproblem_per_task_threshold = "320,80,160,1,80,160,2,20,10,5"
  return hparams