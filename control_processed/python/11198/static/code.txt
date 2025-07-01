def read_binary_matrix(filename):
  """Reads and returns binary formatted matrix stored in filename.

  The file format is described on the data set page:
  https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/

  Args:
    filename: String with path to the file.

  Returns:
    Numpy array contained in the file.
  """
  with tf.io.gfile.GFile(filename, "rb") as f:
    s = f.read()

    # Data is stored in little-endian byte order.
    int32_dtype = np.dtype("int32").newbyteorder("<")

    # The first 4 bytes contain a magic code that specifies the data type.
    magic = int(np.frombuffer(s, dtype=int32_dtype, count=1))
    if magic == 507333717:
      data_dtype = np.dtype("uint8")  # uint8 does not have a byte order.
    elif magic == 507333716:
      data_dtype = np.dtype("int32").newbyteorder("<")
    else:
      raise ValueError("Invalid magic value for data type!")

    # The second 4 bytes contain an int32 with the number of dimensions of the
    # stored array.
    ndim = int(np.frombuffer(s, dtype=int32_dtype, count=1, offset=4))

    # The next ndim x 4 bytes contain the shape of the array in int32.
    dims = np.frombuffer(s, dtype=int32_dtype, count=ndim, offset=8)

    # If the array has less than three dimensions, three int32 are still used to
    # save the shape info (remaining int32 are simply set to 1). The shape info
    # hence uses max(3, ndim) bytes.
    bytes_used_for_shape_info = max(3, ndim) * 4

    # The remaining bytes are the array.
    data = np.frombuffer(
        s, dtype=data_dtype, offset=8 + bytes_used_for_shape_info)
  return data.reshape(tuple(dims))