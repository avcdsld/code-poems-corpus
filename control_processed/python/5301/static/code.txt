def self_attention_expert(x,
                          batch_coordinate,
                          mask_right=True,
                          split_batch=False,
                          attention_num_head=1,
                          attention_kq_size=None,
                          attention_v_size=None):
  """Implementing attention that runs inside each expert.

  Args:
    x: A tensor of shape[batch, depth]. Contains representations from
      different positions, which are lexicographically ordered.
    batch_coordinate: A tensor of shape [batch, 1] containing the batch
      coordinate of each element in x. This is needed to make sure that
      positions from different sequences don't attend to each other.
    mask_right: A bool. If true, we will not attend to positions on the right,
      just as decoder self attention.
    split_batch (bool): If True, each sequence of the batch is processed
      individually on a loop. If False, the sequences are processed all at
      once and a mask is applied to isolate the sequences from each others
    attention_num_head (int): number of attention heads
    attention_kq_size (int): dimension used for the attention key, and query
    attention_v_size (int): dimension used for the attention value

  Returns:
    out: A tensor of shape [batch, depth].
  example use:
  expert_utils.local_moe(
     ...
     expert_fn=functools.partial(self_attention_expert, mask_right=)
     )
  """

  depth = x.get_shape().as_list()[-1]
  length = common_layers.shape_list(batch_coordinate)[0]

  # Print a warning message if one of the expert isn't used (useful at
  # inference where summaries aren't used and the gating function don't add
  # noise)
  global _expert_count  # Hack to make each expert have a unique id
  _expert_count += 1
  length = tf.cond(
      tf.equal(length, 0),
      lambda: tf.Print(  # pylint: disable=g-long-lambda
          length, [length], "Expert {} empty: ".format(_expert_count)),
      lambda: length,
  )

  tf.summary.scalar("batch_size", length, family="experts_stats_batch_size")

  attention_kq_size = attention_kq_size or depth
  attention_v_size = attention_v_size or depth

  def length_not_null(x, batch_coordinate):
    """Branch of the graph only evaluated when length isn't null."""

    # Mask between the sequences (not used if map_ids is used)
    bias_batch = attention_bias_coordinates(batch_coordinate)

    def add_or_set_if(prev_bias, new_bias, condition):
      """Add the bias together while considering the None case."""
      if not condition:
        return prev_bias
      if prev_bias is None:
        return new_bias
      return prev_bias + new_bias

    def mask_and_call_attention(x):
      """Function applied once for each sequence of the batch."""

      # Mask to prevent sequences of attending to the future
      length = common_layers.shape_list(x)[1]  # x has shape [1, length,...]
      bias_past = tf.reshape(
          attention_bias_lower_triangle(length), [length, length])
      # bias has shape [length, length]

      bias = None
      bias = add_or_set_if(bias, bias_past, mask_right)
      bias = add_or_set_if(bias, bias_batch, not split_batch)
      bias = tf.reshape(bias, [1, 1, length, length])

      return multihead_attention(
          x,
          None,
          bias,
          total_key_depth=attention_kq_size,
          total_value_depth=attention_v_size,
          output_depth=depth,
          num_heads=attention_num_head,
          dropout_rate=0.0)

    if split_batch:
      out = expert_utils.map_ids(x, batch_coordinate, mask_and_call_attention)
    else:
      x = tf.reshape(x, [1, length, depth])
      out = mask_and_call_attention(x)
      out = tf.squeeze(out, 0)
    return out

  # If the length is empty, just forward an empty tensor (avoid having to
  # evaluate multihead_attention with tensor having dim equal to zeros)
  out = tf.cond(
      tf.equal(length, 0),
      lambda: tf.zeros(shape=[0, depth], dtype=tf.float32, name="empty_out"),
      lambda: length_not_null(x, batch_coordinate),
  )
  return out