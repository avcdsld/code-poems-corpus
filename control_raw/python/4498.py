def slice_hidden(x, hidden_size, num_blocks):
  """Slice encoder hidden state under num_blocks.

  Args:
    x: Encoder hidden state of shape [batch_size, latent_dim, hidden_size].
    hidden_size: Dimension of the latent space.
    num_blocks: Number of blocks in DVQ.

  Returns:
    Sliced states of shape [batch_size, latent_dim, num_blocks, block_dim].
  """
  batch_size, latent_dim, _ = common_layers.shape_list(x)
  block_dim = hidden_size // num_blocks
  x_sliced = tf.reshape(x,
                        shape=[batch_size, latent_dim, num_blocks, block_dim])
  return x_sliced