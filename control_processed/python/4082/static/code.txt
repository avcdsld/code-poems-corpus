def sparse_tensor_value_to_texts(value, alphabet):
    r"""
    Given a :class:`tf.SparseTensor` ``value``, return an array of Python strings
    representing its values, converting tokens to strings using ``alphabet``.
    """
    return sparse_tuple_to_texts((value.indices, value.values, value.dense_shape), alphabet)