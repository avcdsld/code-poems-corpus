def reduce_to_2d(arr):
  """Given a np.npdarray with nDims > 2, reduce it to 2d.

  It does this by selecting the zeroth coordinate for every dimension greater
  than two.

  Args:
    arr: a numpy ndarray of dimension at least 2.

  Returns:
    A two-dimensional subarray from the input array.

  Raises:
    ValueError: If the argument is not a numpy ndarray, or the dimensionality
      is too low.
  """
  if not isinstance(arr, np.ndarray):
    raise ValueError('reduce_to_2d requires a numpy.ndarray')

  ndims = len(arr.shape)
  if ndims < 2:
    raise ValueError('reduce_to_2d requires an array of dimensionality >=2')
  # slice(None) is equivalent to `:`, so we take arr[0,0,...0,:,:]
  slices = ([0] * (ndims - 2)) + [slice(None), slice(None)]
  return arr[slices]