def super_lm_base():
  """Set of hyperparameters."""
  hparams = common_hparams.basic_params1()
  hparams.hidden_size = 512
  hparams.moe_hidden_sizes = "512"
  hparams.batch_size = 16384
  hparams.max_length = 0
  # All hyperparameters ending in "dropout" are automatically set to 0.0
  # when not in training mode.
  hparams.layer_prepostprocess_dropout = 0.0
  hparams.symbol_dropout = 0.1
  hparams.add_hparam("attention_dropout", 0.0)
  hparams.label_smoothing = 0.0
  hparams.clip_grad_norm = 0.  # i.e. no gradient clipping
  hparams.optimizer = "Adafactor"
  hparams.learning_rate_decay_scheme = "noam"
  hparams.learning_rate = 0.1
  hparams.learning_rate_warmup_steps = 8000
  hparams.initializer_gain = 1.0
  hparams.initializer = "uniform_unit_scaling"
  hparams.weight_decay = 0.0
  hparams.shared_embedding_and_softmax_weights = False
  hparams.layer_preprocess_sequence = "n"
  hparams.layer_postprocess_sequence = "da"
  # we only want one data shard.
  hparams.no_data_parallelism = True
  # bypass the symbol modality so that we can use model parallelism.
  hparams.bottom = {
      "inputs": modalities.identity_bottom,
      "targets": modalities.identity_bottom,
  }
  hparams.top = {
      "targets": modalities.identity_top,
  }
  hparams.add_hparam("filter_size", 512)
  hparams.add_hparam("mix_fraction", 0.5)
  # attention-related flags
  hparams.add_hparam("multihead_attention_num_heads", 4)
  hparams.add_hparam("multihead_attention_key_channels", 0)
  hparams.add_hparam("multihead_attention_value_channels", 0)
  hparams.add_hparam("pos", "timing")  # timing, none
  hparams.add_hparam(
      "layers", ("n,att,m,d,a," "n,ffn,m,d,a,") * 4 + "n,ffn,d")
  # Number of model shards - each one has separate parameters.
  # Changing this number invalidates checkpoints.
  hparams.add_hparam("num_model_shards", 8)
  hparams.add_hparam("diet_experts", False)
  return hparams