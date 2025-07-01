def ffn_layer(x, hparams, losses=None):
  """ffn layer transformer."""
  with tf.variable_scope("ffn"):
    if hparams.ffn_layer == "none":
      return x
    if hparams.ffn_layer == "conv_hidden_relu":
      y = common_layers.dense_relu_dense(
          x,
          hparams.filter_size,
          hparams.hidden_size,
          dropout=hparams.relu_dropout)
    elif hparams.ffn_layer == "normed_conv_hidden_relu":
      y = common_layers.normed_conv_hidden_relu(
          x,
          hparams.norm_type,
          hparams.layer_norm_epsilon,
          hparams.filter_size,
          hparams.hidden_size,
          dropout=hparams.relu_dropout,
          norm_name="convnorm")
    elif hparams.ffn_layer == "self_attention_ffn":
      x_shape = tf.shape(x)
      x = tf.reshape(x, [x_shape[0], -1, hparams.hidden_size])
      y = common_attention.ffn_self_attention_layer(
          x, hparams.filter_size, hparams.hidden_size, hparams.num_parts,
          hparams.attention_dropout, hparams.share_kv)
      y = tf.reshape(y, x_shape)
    elif hparams.ffn_layer == "local_moe_tpu":
      overhead = (hparams.moe_overhead_train
                  if hparams.mode == tf.estimator.ModeKeys.TRAIN
                  else hparams.moe_overhead_eval)
      x, x_shape, is_4d = maybe_reshape_4d_to_3d(x)
      y, loss = expert_utils.local_moe_tpu(
          x, hparams.filter_size // 2,
          hparams.hidden_size,
          hparams.moe_num_experts, overhead=overhead,
          loss_coef=hparams.moe_loss_coef)
      if is_4d:
        y = tf.reshape(y, x_shape)
      if losses is None:
        raise ValueError(
            "transformer_ffn_layer with type local_moe_tpu must pass in "
            "a losses list")
      losses.append(loss)
    else:
      assert hparams.ffn_layer == "glu_ffn"
      y = common_layers.gated_linear_unit_layer(x)
    return y