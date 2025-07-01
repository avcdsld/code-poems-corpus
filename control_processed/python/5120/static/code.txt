def multihead_mpnn_attention(node_states,
                             total_key_depth,
                             total_value_depth,
                             output_depth,
                             num_heads,
                             adjacency_matrix=None,
                             num_edge_types=5,
                             num_transforms=None,
                             use_weighted_sum=False,
                             name="mpnn_attention"):
  """Multihead scaled-dot-product attention with input/output transformations.

  Let B be the number of batches.
  Let N be the number of nodes in the graph.
  Let D be the size of the node hidden states.
  Let K be the size of the attention keys/queries (total_key_depth).
  Let V be the size of the attention values (total_value_depth).
  Let O be the size of the attention output (output_depth).
  Let H be the number of heads (num_heads).
  Let T be the total number of transforms (num_transforms).

  The key and value depths are split across all of the heads. For example, if
  the key depth is 6 and there are three heads, then the key for each head has
  depth 2.

  Args:
    node_states: A Tensor with shape [B, N, D]
    total_key_depth: An integer (K).
    total_value_depth: An integer (V).
    output_depth: An integer (O).
    num_heads: An integer (H).
    adjacency_matrix: An Tensor of ints with shape [B, T, N, N]. If there is an
      edge from node j to node i in batch b, then adjacency_matrix[b, i, j]
      contains the type of that edge as an integer. Otherwise, it contains 0.
    num_edge_types: An integer indicating number of edge types.
    num_transforms: An integer indicating number of transforms (T). If None,
      then num_transforms will be equal to num_edge_types.
    use_weighted_sum: If False, will only use a single transform per edge type.
      Otherwise, use a learned weighted sum of transforms per edge type.
    name: A string.

  Returns:
    The result of the attention transformation. The output shape is [B, N, O].

  Raises:
    ValueError: if the key depth or value depth are not divisible by the
      number of attention heads.
  """
  if total_key_depth % num_heads != 0:
    raise ValueError("Key depth (%d) must be divisible by the number of "
                     "attention heads (%d)." % (total_key_depth, num_heads))
  if total_value_depth % num_heads != 0:
    raise ValueError("Value depth (%d) must be divisible by the number of "
                     "attention heads (%d)." % (total_value_depth, num_heads))
  with tf.variable_scope(
      name, default_name="multihead_mpnn_attention", values=[node_states]):
    # If not explicitly set, use num_transforms set to num_edge_types.
    num_transforms = (
        num_edge_types if num_transforms is None else num_transforms)

    # Create the query for each node's incoming edges.
    # Create the keys/values for each node for each possible outgoing edge type.
    q, k, v = compute_mpnn_qkv(
        node_states,
        total_key_depth,
        total_value_depth,
        num_transforms)

    q_shape = tf.shape(q)  # As above, q_shape is [B, N, K].

    # Divides each query/key/value into separate heads. Specifically, the
    # query/key/value for each (batch, node) pair (i.e., the third dimensions
    # of q, k, and v) are broken into H separate pieces. These pieces are used
    # as the separate attention heads. The resulting tensors have shape
    # [B, H, N, ?/H], where ? = K, K*T or V*T as appropriate.
    q = common_attention.split_heads(q, num_heads)  # Shape [B, H, N, K/H].
    k = common_attention.split_heads(k, num_heads)  # Shape [B, H, N, K*T/H].
    v = common_attention.split_heads(v, num_heads)  # Shape [B, H, N, V*T/H].
    key_depth_per_head = total_key_depth // num_heads

    # Ensures that the logits don't have too large of a magnitude.
    q *= key_depth_per_head**-0.5

    # Rearrange the dimensions so that the head is first. This will make
    # subsequent steps easier (we loop over the head).
    q = tf.transpose(q, [1, 0, 2, 3])  # Shape [H, B, N, K/H].
    k = tf.transpose(k, [1, 0, 2, 3])  # Shape [H, B, N, K*T/H].
    v = tf.transpose(v, [1, 0, 2, 3])  # Shape [H, B, N, V*T/H].

    # Split the keys and values into separate per-edge-type keys and values.
    k = tf.reshape(k, [
        num_heads, q_shape[0], q_shape[1], num_transforms,
        total_key_depth // num_heads
    ])  # Shape [H, B, N, T, K/H].
    k = tf.transpose(k, [0, 1, 3, 2, 4])  # Shape [H, B, T, N, K/H].

    v = tf.reshape(v, [
        num_heads, q_shape[0], q_shape[1], num_transforms,
        total_value_depth // num_heads
    ])  # Shape [H, B, N, T, V/H].
    v = tf.transpose(v, [0, 1, 3, 2, 4])  # Shape [H, B, T, N, V/H].

    # Perform attention for each head and combine the results into a list.
    # head_outputs stores a list of tensors, each with shape [1, B, N, V/H].
    # The last dimension contains the values computed for each attention head.
    # Each value was determined by computing attention over all of the
    # incoming edges for node n, weighting the incoming values accordingly,
    # and adding those weighted values together.
    head_outputs = []
    for head_id in range(num_heads):
      output = dot_product_mpnn_attention(
          q[head_id],
          k[head_id],
          v[head_id],
          adjacency_matrix,
          num_edge_types,
          num_transforms=num_transforms,
          use_weighted_sum=use_weighted_sum)

      # Store this result in the list of attention results for each head.
      # The call to expand_dims gives output shape [1, B, N, V/H], which will
      # come in handy when we combine the heads together.
      head_outputs.append(tf.expand_dims(output, axis=0))

    # Combine the heads together into one tensor and rearrange the dimensions.
    x = tf.concat(head_outputs, axis=0)  # Shape [H, B, N, V/H].
    x = tf.transpose(x, [1, 0, 2, 3])  # Shape [B, H, N, V/H].

    # Concatenate the values produced by each head together into one vector.
    x = common_attention.combine_heads(x)  # Shape [B, N, V].

    # A fully-connected linear layer to convert from the value vectors of size V
    # to output vectors of length O (the appropriate output length).
    x = common_layers.dense(
        x, output_depth, use_bias=False, name="output_transform")
    return x