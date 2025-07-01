def is_compatible_with(self, spec_or_tensor):
    """Returns True if spec_or_tensor is compatible with this TensorSpec.

    Two tensors are considered compatible if they have the same dtype
    and their shapes are compatible (see `tf.TensorShape.is_compatible_with`).

    Args:
      spec_or_tensor: A tf.TensorSpec or a tf.Tensor

    Returns:
      True if spec_or_tensor is compatible with self.
    """
    return (self._dtype.is_compatible_with(spec_or_tensor.dtype) and
            self._shape.is_compatible_with(spec_or_tensor.shape))