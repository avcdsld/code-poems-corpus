def make_2d_block_raster_mask(query_shape, memory_flange):
  """Creates a mask for 2d block raster scan.

  The query mask can look to the left, top left, top, and top right, but
  not to the right. Inside the query, we have the standard raster scan
  masking.
  Args:
    query_shape: A tuple of ints (query_height, query_width)
    memory_flange: A tuple of ints
      (memory_flange_height, memory_flange_width)

  Returns:
    A tensor of shape query_size, memory_size
  """
  # mask inside the query block
  query_triangle = common_layers.ones_matrix_band_part(
      np.prod(query_shape), np.prod(query_shape), -1, 0)
  split_query_masks = tf.split(query_triangle, query_shape[0], axis=1)
  # adding mask for left and right
  mask_pieces = [
      tf.concat(  # pylint: disable=g-complex-comprehension
          [tf.ones([np.prod(query_shape), memory_flange[1]]),
           split_query_masks[i],
           tf.zeros([np.prod(query_shape), memory_flange[1]])],
          axis=1) for i in range(query_shape[0])
  ]
  # adding mask for top
  final_mask = tf.concat(
      [
          tf.ones([
              np.prod(query_shape),
              (query_shape[1] + 2 * memory_flange[1]) * memory_flange[0]
          ]),
          tf.concat(mask_pieces, axis=1)
      ],
      axis=1)
  # 0.0 is visible location, 1.0 is masked.
  return 1. - final_mask