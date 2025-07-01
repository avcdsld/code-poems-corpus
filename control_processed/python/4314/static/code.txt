def vqa_self_attention_base():
  """VQA attention baseline hparams."""
  hparams = common_hparams.basic_params1()
  hparams.batch_size = 128
  hparams.use_fixed_batch_size = True,
  hparams.optimizer = "adam"
  hparams.optimizer_adam_beta1 = 0.9
  hparams.optimizer_adam_beta2 = 0.997
  hparams.optimizer_adam_epsilon = 1e-9
  hparams.weight_decay = 0.
  hparams.clip_grad_norm = 0.
  hparams.initializer = "xavier"
  hparams.learning_rate_schedule = (
      "constant*linear_warmup*rsqrt_normalized_decay")
  hparams.learning_rate_warmup_steps = 8000
  hparams.learning_rate_constant = 1e-3
  hparams.learning_rate_decay_rate = 0.5
  hparams.learning_rate_decay_steps = 50000
  hparams.dropout = 0.5
  hparams.summarize_grads = True
  hparams.summarize_vars = True

  # not used hparams
  hparams.label_smoothing = 0.
  hparams.multiply_embedding_mode = "sqrt_depth"

  # add new hparams
  # use raw image as input
  hparams.add_hparam("image_input_type", "image")
  hparams.add_hparam("image_model_fn", "resnet_v1_152")
  hparams.add_hparam("resize_side", 512)
  hparams.add_hparam("height", 448)
  hparams.add_hparam("width", 448)
  hparams.add_hparam("distort", True)
  hparams.add_hparam("train_resnet", False)

  # image parts
  hparams.add_hparam("image_feat_preprocess_proj", True)
  hparams.add_hparam("image_feat_preprocess_layernorm", True)
  hparams.add_hparam("image_feat_encode", True)
  hparams.add_hparam("image_hidden_size", 0)  # default to hidden_size
  hparams.add_hparam("image_filter_size", 0)  # defaults to filter_size

  # question hidden size
  hparams.hidden_size = 512
  hparams.filter_size = 1024
  hparams.num_hidden_layers = 4

  hparams.add_hparam("multimodal_combine", "concat")
  hparams.add_hparam("num_mlp_layers", 1)
  hparams.add_hparam("mlp_size", 1024)

  # self attention parts
  hparams.norm_type = "layer"
  hparams.layer_preprocess_sequence = "n"
  hparams.layer_postprocess_sequence = "da"
  hparams.layer_prepostprocess_dropout = 0.1
  hparams.attention_dropout = 0.1
  hparams.relu_dropout = 0.1
  hparams.add_hparam("pos", "timing")
  hparams.add_hparam("num_encoder_layers", 0)
  hparams.add_hparam("num_decoder_layers", 0)
  hparams.add_hparam("num_heads", 8)
  hparams.add_hparam("attention_key_channels", 0)
  hparams.add_hparam("attention_value_channels", 0)
  hparams.add_hparam("self_attention_type", "dot_product")
  hparams.add_hparam("image_self_attention_type", "dot_product")
  hparams.add_hparam("question_self_attention_type", "dot_product")
  hparams.add_hparam("block_length", 1)
  hparams.add_hparam("scale_dotproduct", True)

  # iterative part
  hparams.add_hparam("num_rec_steps", 3)

  return hparams