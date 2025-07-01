def int_to_bit(self, x_int, num_bits, base=2):
    """Turn x_int representing numbers into a bitwise (lower-endian) tensor.

    Args:
        x_int: Tensor containing integer to be converted into base
        notation.
        num_bits: Number of bits in the representation.
        base: Base of the representation.

    Returns:
        Corresponding number expressed in base.
    """
    x_l = tf.to_int32(tf.expand_dims(x_int, axis=-1))
    # pylint: disable=g-complex-comprehension
    x_labels = [
        tf.floormod(
            tf.floordiv(tf.to_int32(x_l),
                        tf.to_int32(base)**i), tf.to_int32(base))
        for i in range(num_bits)]
    res = tf.concat(x_labels, axis=-1)
    return tf.to_float(res)