def _minimize_and_clip(optimizer, objective, var_list, clip_val=10):
    """Minimized `objective` using `optimizer` w.r.t. variables in
    `var_list` while ensure the norm of the gradients for each
    variable is clipped to `clip_val`
    """
    gradients = optimizer.compute_gradients(objective, var_list=var_list)
    for i, (grad, var) in enumerate(gradients):
        if grad is not None:
            gradients[i] = (tf.clip_by_norm(grad, clip_val), var)
    return gradients