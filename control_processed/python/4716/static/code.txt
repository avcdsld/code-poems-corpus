def ae_transformer_internal(inputs, targets, target_space, hparams, cache=None):
  """Main step used for training."""
  # Encoder.
  inputs = common_layers.flatten4d3d(inputs)
  inputs, ed = encode(inputs, target_space, hparams, "input_enc")

  # Autoencoding.
  losses = {"extra": tf.constant(0.0), "latent_pred": tf.constant(0.0)}

  max_targets_len_from_inputs = tf.concat([inputs, inputs], axis=1)
  targets, _ = common_layers.pad_to_same_length(
      targets,
      max_targets_len_from_inputs,
      final_length_divisible_by=2**hparams.num_compress_steps)
  targets_c = compress(targets, hparams, "compress")
  if hparams.mode != tf.estimator.ModeKeys.PREDICT:
    # Compress and bottleneck.
    latents_discrete_hot, extra_loss = vq_discrete_bottleneck(
        x=targets_c, hparams=hparams)
    latents_dense = vq_discrete_unbottleneck(
        latents_discrete_hot, hparams=hparams)
    latents_dense = targets_c + tf.stop_gradient(latents_dense - targets_c)
    latents_discrete = tf.argmax(latents_discrete_hot, axis=-1)
    tf.summary.histogram("codes", tf.reshape(latents_discrete[:, 0, :], [-1]))
    losses["extra"] = extra_loss

    # Extra loss predicting latent code from input.
    latents_pred = decode_transformer(inputs, ed, latents_dense, hparams,
                                      "extra")
    latent_pred_loss = get_latent_pred_loss(latents_pred, latents_discrete_hot,
                                            hparams)
    losses["latent_pred"] = tf.reduce_mean(latent_pred_loss)
  else:
    latent_len = common_layers.shape_list(targets_c)[1]
    embed = functools.partial(vq_discrete_unbottleneck, hparams=hparams)
    latents_dense = tf.zeros_like(targets_c[:, :latent_len, :, :])
    if cache is None:
      cache = ae_latent_sample_beam(latents_dense, inputs, ed, embed,
                                    hparams)
    cache_hot = tf.one_hot(cache, depth=2**hparams.bottleneck_bits)
    latents_dense = embed(cache_hot)

  # Postprocess.
  d = latents_dense
  pos = tf.get_variable("pos", [1, 1000, 1, hparams.hidden_size])
  pos = pos[:, :common_layers.shape_list(latents_dense)[1] + 1, :, :]
  latents_dense = tf.pad(latents_dense, [[0, 0], [1, 0], [0, 0], [0, 0]]) + pos

  # Decompressing the dense latents
  for i in range(hparams.num_compress_steps):
    j = hparams.num_compress_steps - i - 1
    d = residual_conv(d, 1, (3, 1), hparams, "decompress_rc_%d" % j)
    d = decompress_step(d, hparams, i > 0, "decompress_%d" % j)

  masking = common_layers.inverse_lin_decay(hparams.mask_startup_steps)
  masking *= common_layers.inverse_exp_decay(
      hparams.mask_startup_steps // 4)  # Not much at start.
  masking = tf.minimum(tf.maximum(masking, 0.0), 1.0)
  if hparams.mode == tf.estimator.ModeKeys.PREDICT:
    masking = 1.0
  mask = tf.less(masking,
                 tf.random_uniform(common_layers.shape_list(targets)[:-1]))
  mask = tf.expand_dims(tf.to_float(mask), 3)

  # targets is always [batch, length, 1, depth]
  targets = mask * targets + (1.0 - mask) * d

  res = decode_transformer(inputs, ed, targets, hparams, "decoder")
  latent_time = tf.less(hparams.mask_startup_steps,
                        tf.to_int32(tf.train.get_global_step()))
  losses["latent_pred"] *= tf.to_float(latent_time)
  return res, losses, cache