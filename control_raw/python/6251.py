def tensors_equal(tensor1: torch.Tensor, tensor2: torch.Tensor, tolerance: float = 1e-12) -> bool:
    """
    A check for tensor equality (by value).  We make sure that the tensors have the same shape,
    then check all of the entries in the tensor for equality.  We additionally allow the input
    tensors to be lists or dictionaries, where we then do the above check on every position in the
    list / item in the dictionary.  If we find objects that aren't tensors as we're doing that, we
    just defer to their equality check.

    This is kind of a catch-all method that's designed to make implementing ``__eq__`` methods
    easier, in a way that's really only intended to be useful for tests.
    """
    # pylint: disable=too-many-return-statements
    if isinstance(tensor1, (list, tuple)):
        if not isinstance(tensor2, (list, tuple)) or len(tensor1) != len(tensor2):
            return False
        return all([tensors_equal(t1, t2, tolerance) for t1, t2 in zip(tensor1, tensor2)])
    elif isinstance(tensor1, dict):
        if not isinstance(tensor2, dict):
            return False
        if tensor1.keys() != tensor2.keys():
            return False
        return all([tensors_equal(tensor1[key], tensor2[key], tolerance) for key in tensor1])
    elif isinstance(tensor1, torch.Tensor):
        if not isinstance(tensor2, torch.Tensor):
            return False
        if tensor1.size() != tensor2.size():
            return False
        return ((tensor1 - tensor2).abs().float() < tolerance).all()
    else:
        try:
            return tensor1 == tensor2
        except RuntimeError:
            print(type(tensor1), type(tensor2))
            raise