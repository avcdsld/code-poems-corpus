def gumbel_softmax_nearest_neighbor_dvq(x,
                                        means,
                                        block_v_size,
                                        hard=False,
                                        temperature_init=1.2,
                                        num_samples=1,
                                        temperature_warmup_steps=150000,
                                        summary=True,
                                        num_flows=0,
                                        approximate_gs_entropy=False,
                                        sum_over_latents=False):
  """Sample from Gumbel-Softmax and compute neighbors and losses.

  Args:
    x: A `float`-like `Tensor` of shape [batch_size, latent_dim, num_blocks,
      block_dim] containing the latent vectors to be compared to the codebook.
    means: Embedding table of shape [num_blocks, block_v_size, block_dim].
    block_v_size: Number of discrete codes per block.
    hard: Determines whether we take hard or soft Gumbel-Softmax samples
      (Default: False).
    temperature_init: Initial temperature used for Gumbel-Softmax samples,
      after it which it decays to 0 (Default: 1.2).
    num_samples: Number of samples drawn for each latent (Default: 1).
    temperature_warmup_steps: Number of steps it takes to decay temperature to 0
      (Default: 150000).
    summary: When `True`, we save histogram summaries of the KL term (Default:
      True).
    num_flows: Number of inverse autoregressive flows with Gumbel-Softmax
      samples.
    approximate_gs_entropy: When `True`, we approximate Gumbel-Softmax
      density as categorical when calculating sample entropy (Default: False).
    sum_over_latents: Whether to sum over non-batch dimensions when calculating
      negative entropy loss.

  Returns:
    x_means_assignments: A `float`-like `Tensor` containing the codebook
      assignments, averaged over samples, with shape [batch_size * latent_dim,
      num_blocks, block_v_size].
    neg_q_entropy: The negative entropy of the variational distribution,
      averaged over samples.
  """
  batch_size, latent_dim, num_blocks, block_dim = common_layers.shape_list(x)

  # Combine latent_dim and batch_size for computing distances.
  x = tf.reshape(x, [-1, num_blocks, block_dim])

  # Compute distances using (x - means)**2 = x**2 + means**2 - 2*x*means.
  x_norm_sq = tf.reduce_sum(tf.square(x), axis=-1, keepdims=True)
  means_norm_sq = tf.reduce_sum(tf.square(means), axis=-1, keepdims=True)
  means_norm_sq = tf.transpose(means_norm_sq, perm=[2, 0, 1])
  scalar_prod = tf.matmul(
      tf.transpose(x, perm=[1, 0, 2]), tf.transpose(means, perm=[0, 2, 1]))
  scalar_prod = tf.transpose(scalar_prod, perm=[1, 0, 2])
  dist = x_norm_sq + means_norm_sq - 2 * scalar_prod

  # IAF requires latents to have their own dimension, so reshape dist from
  # [batch_size * latent_dim, num_blocks, block_v_size] to
  # [batch_size * num_blocks, latent_dim, block_v_size].
  dist = tf.reshape(dist, [batch_size, latent_dim, num_blocks, -1])
  dist = tf.reshape(
      tf.transpose(dist, perm=[0, 2, 1, 3]), [-1, latent_dim, block_v_size])
  log_class_probs = tf.nn.log_softmax(-dist)

  sample_shape = [num_samples] + common_layers.shape_list(dist)
  gumbel_samples = gumbel_sample(sample_shape)

  # Temperature decays linearly.
  temperature = temperature_init - common_layers.inverse_lin_decay(
      temperature_warmup_steps)

  # 10% of the time keep reasonably high temperature to keep learning.
  temperature = tf.cond(
      tf.less(tf.random_uniform([]), 0.9), lambda: temperature,
      lambda: tf.random_uniform([], minval=0.5, maxval=1.0))

  gumbel_softmax_samples = tf.nn.softmax(
      (tf.expand_dims(log_class_probs, 0) + gumbel_samples) / temperature)
  q_samples = tf.clip_by_value(gumbel_softmax_samples, 1e-6, 1 - 1e-6)

  if approximate_gs_entropy:
    q_dist = tfp.distributions.Multinomial(total_count=1.0, logits=-dist)
  else:
    q_dist = tfp.distributions.RelaxedOneHotCategorical(
        temperature, logits=-dist)

  # Take mean over samples to approximate entropy.
  neg_q_entropy = tf.reduce_mean(q_dist.log_prob(q_samples), 0)
  if summary:
    tf.summary.histogram("neg_q_entropy", tf.reshape(neg_q_entropy, [-1]))
  if sum_over_latents:
    neg_q_entropy = tf.reshape(neg_q_entropy,
                               [batch_size, num_blocks, latent_dim])
    neg_q_entropy = tf.reduce_sum(neg_q_entropy, [1, 2])
  neg_q_entropy = tf.reduce_mean(neg_q_entropy)

  if num_flows > 0:
    hparams = iaf_hparams(hidden_size=512, filter_size=4096)
    q_samples = tf.reshape(q_samples, [-1, latent_dim, block_v_size])
    for flow in range(num_flows):
      shifted_samples = tf.pad(q_samples, [[0, 0], [1, 0], [0, 0]])[:, :-1, :]

      # Project samples from  [batch_size, latent_size, block_v_size] to
      # [batch_size, latent_size, hidden_size].
      shifted_samples = common_layers.dense(shifted_samples,
                                            hparams.hidden_size)
      # TODO(vafa): Include masking as a flag.
      mask = True
      if mask:
        attention_type = cia.AttentionType.LOCAL_1D
      else:
        attention_type = cia.AttentionType.GLOBAL
      ffn_output = cia.transformer_decoder_layers(
          inputs=shifted_samples,
          encoder_output=None,
          num_layers=6,
          hparams=hparams,
          attention_type=attention_type,
          name="transformer_" + str(flow))

      # Project samples back to [batch_size, latent_size, block_v_size].
      ffn_output = common_layers.dense(ffn_output, block_v_size)
      log_pi = tf.nn.log_softmax(ffn_output)

      # Flow 1: Adding log_pi to q_samples and dividing by the temperature.
      # Note that we drop the last dimension of q_samples for centered-softmax,
      # which we can do without recalculating probabilities because the last
      # dimension of log_pi and q_samples are deterministic given the others.
      # Flow 2: Centered-softmax.
      chained_bijectors = tfp.bijectors.Chain([
          tfp.bijectors.SoftmaxCentered(),
          tfp.bijectors.Affine(
              shift=log_pi[:, :, :-1],
              scale_identity_multiplier=1. / temperature)
      ])
      q_samples = chained_bijectors.forward(q_samples[:, :, :-1])
      log_det = chained_bijectors.inverse_log_det_jacobian(
          q_samples, event_ndims=1)
      log_det = tf.reshape(log_det,
                           [num_samples, batch_size, num_blocks, latent_dim])
      if sum_over_latents:
        log_det = tf.reduce_sum(log_det, axis=[2, 3])
      neg_q_entropy += tf.reduce_mean(log_det)

    q_samples = tf.reshape(
        q_samples,
        [num_samples, batch_size * num_blocks, latent_dim, block_v_size])

  if hard:
    x_means_idx = tf.argmax(q_samples, -1)

    # Take average of one-hot vectors over samples.
    x_means_hot = tf.reduce_mean(tf.one_hot(x_means_idx, block_v_size), 0)
    x_means_assignments = (
        tf.reduce_mean(q_samples, 0) +
        tf.stop_gradient(x_means_hot - tf.reduce_mean(q_samples, 0)))
  else:
    x_means_assignments = tf.reduce_mean(gumbel_softmax_samples, 0)

  # Reshape assignments to [batch_size * latent_dim, num_blocks,
  # block_v_size]. We have to transpose between reshapes to make sure the
  # dimensions have the correct interpretation.
  x_means_assignments = tf.reshape(
      x_means_assignments, [batch_size, num_blocks, latent_dim, block_v_size])
  x_means_assignments = tf.transpose(x_means_assignments, [0, 2, 1, 3])
  x_means_assignments = tf.reshape(
      x_means_assignments, [batch_size * latent_dim, num_blocks, block_v_size])

  return x_means_assignments, neg_q_entropy