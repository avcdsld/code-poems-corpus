def merge_grad_list(all_grads, all_vars):
    """
    Args:
        all_grads (K x N): gradients
        all_vars(K x N): variables

    Return:
        K x N x 2: list of list of (grad, var) pairs
    """
    return [list(zip(gs, vs)) for gs, vs in zip(all_grads, all_vars)]