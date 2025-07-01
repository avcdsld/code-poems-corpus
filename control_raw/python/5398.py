def local_attention_1d(x,
                       hparams,
                       attention_type="local_unmasked",
                       q_padding="VALID",
                       kv_padding="VALID"):
  """Local 1d self attention."""
  # self-attention
  x, x_shape, is_4d = maybe_reshape_4d_to_3d(x)
  with tf.variable_scope("local_1d_self_att"):
    y = common_attention.multihead_attention(
        x,
        None,
        None,
        hparams.attention_key_channels or hparams.hidden_size,
        hparams.attention_value_channels or hparams.hidden_size,
        hparams.hidden_size,
        hparams.num_heads,
        hparams.attention_dropout,
        attention_type=attention_type,
        shared_rel=hparams.shared_rel,
        block_width=hparams.block_width,
        block_length=hparams.block_length,
        q_padding=q_padding,
        kv_padding=kv_padding,
        q_filter_width=hparams.q_filter_width,
        kv_filter_width=hparams.kv_filter_width,
        make_image_summary=False,
        name="self_attention")
    if is_4d:
      y = tf.reshape(y, x_shape)
    return y