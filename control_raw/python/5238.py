def add_positional_embedding_nd(x, max_length, name=None):
  """Adds n-dimensional positional embedding.

  The embeddings add to all positional dimensions of the tensor.

  Args:
    x: Tensor with shape [batch, p1 ... pn, depth]. It has n positional
      dimensions, i.e., 1 for text, 2 for images, 3 for video, etc.
    max_length: int representing static maximum size of any dimension.
    name: str representing name of the embedding tf.Variable.

  Returns:
    Tensor of same shape as x.
  """
  with tf.name_scope("add_positional_embedding_nd"):
    x_shape = common_layers.shape_list(x)
    num_dims = len(x_shape) - 2
    depth = x_shape[-1]
    base_shape = [1] * (num_dims + 1) + [depth]
    base_start = [0] * (num_dims + 2)
    base_size = [-1] + [1] * num_dims + [depth]
    for i in range(num_dims):
      shape = base_shape[:]
      start = base_start[:]
      size = base_size[:]
      shape[i + 1] = max_length
      size[i + 1] = x_shape[i + 1]
      var = tf.get_variable(
          name + "_%d" % i,
          shape,
          initializer=tf.random_normal_initializer(0, depth**-0.5))
      var = var * depth**0.5
      x += tf.slice(var, start, size)
    return x