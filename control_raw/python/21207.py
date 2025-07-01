def make_ndarray(tensor):
    """Create a numpy ndarray from a tensor.

  Create a numpy ndarray with the same shape and data as the tensor.

  Args:
    tensor: A TensorProto.

  Returns:
    A numpy array with the tensor contents.

  Raises:
    TypeError: if tensor has unsupported type.

  """
    shape = [d.size for d in tensor.tensor_shape.dim]
    num_elements = np.prod(shape, dtype=np.int64)
    tensor_dtype = dtypes.as_dtype(tensor.dtype)
    dtype = tensor_dtype.as_numpy_dtype

    if tensor.tensor_content:
        return np.frombuffer(tensor.tensor_content, dtype=dtype).copy().reshape(shape)
    elif tensor_dtype == dtypes.float16 or tensor_dtype == dtypes.bfloat16:
        # the half_val field of the TensorProto stores the binary representation
        # of the fp16: we need to reinterpret this as a proper float16
        if len(tensor.half_val) == 1:
            tmp = np.array(tensor.half_val[0], dtype=np.uint16)
            tmp.dtype = tensor_dtype.as_numpy_dtype
            return np.repeat(tmp, num_elements).reshape(shape)
        else:
            tmp = np.fromiter(tensor.half_val, dtype=np.uint16)
            tmp.dtype = tensor_dtype.as_numpy_dtype
            return tmp.reshape(shape)
    elif tensor_dtype == dtypes.float32:
        if len(tensor.float_val) == 1:
            return np.repeat(
                np.array(tensor.float_val[0], dtype=dtype), num_elements
            ).reshape(shape)
        else:
            return np.fromiter(tensor.float_val, dtype=dtype).reshape(shape)
    elif tensor_dtype == dtypes.float64:
        if len(tensor.double_val) == 1:
            return np.repeat(
                np.array(tensor.double_val[0], dtype=dtype), num_elements
            ).reshape(shape)
        else:
            return np.fromiter(tensor.double_val, dtype=dtype).reshape(shape)
    elif tensor_dtype in [
        dtypes.int32,
        dtypes.uint8,
        dtypes.uint16,
        dtypes.int16,
        dtypes.int8,
        dtypes.qint32,
        dtypes.quint8,
        dtypes.qint8,
        dtypes.qint16,
        dtypes.quint16,
    ]:
        if len(tensor.int_val) == 1:
            return np.repeat(
                np.array(tensor.int_val[0], dtype=dtype), num_elements
            ).reshape(shape)
        else:
            return np.fromiter(tensor.int_val, dtype=dtype).reshape(shape)
    elif tensor_dtype == dtypes.int64:
        if len(tensor.int64_val) == 1:
            return np.repeat(
                np.array(tensor.int64_val[0], dtype=dtype), num_elements
            ).reshape(shape)
        else:
            return np.fromiter(tensor.int64_val, dtype=dtype).reshape(shape)
    elif tensor_dtype == dtypes.string:
        if len(tensor.string_val) == 1:
            return np.repeat(
                np.array(tensor.string_val[0], dtype=dtype), num_elements
            ).reshape(shape)
        else:
            return np.array([x for x in tensor.string_val], dtype=dtype).reshape(shape)
    elif tensor_dtype == dtypes.complex64:
        it = iter(tensor.scomplex_val)
        if len(tensor.scomplex_val) == 2:
            return np.repeat(
                np.array(
                    complex(tensor.scomplex_val[0], tensor.scomplex_val[1]), dtype=dtype
                ),
                num_elements,
            ).reshape(shape)
        else:
            return np.array(
                [complex(x[0], x[1]) for x in zip(it, it)], dtype=dtype
            ).reshape(shape)
    elif tensor_dtype == dtypes.complex128:
        it = iter(tensor.dcomplex_val)
        if len(tensor.dcomplex_val) == 2:
            return np.repeat(
                np.array(
                    complex(tensor.dcomplex_val[0], tensor.dcomplex_val[1]), dtype=dtype
                ),
                num_elements,
            ).reshape(shape)
        else:
            return np.array(
                [complex(x[0], x[1]) for x in zip(it, it)], dtype=dtype
            ).reshape(shape)
    elif tensor_dtype == dtypes.bool:
        if len(tensor.bool_val) == 1:
            return np.repeat(
                np.array(tensor.bool_val[0], dtype=dtype), num_elements
            ).reshape(shape)
        else:
            return np.fromiter(tensor.bool_val, dtype=dtype).reshape(shape)
    else:
        raise TypeError("Unsupported tensor type: %s" % tensor.dtype)