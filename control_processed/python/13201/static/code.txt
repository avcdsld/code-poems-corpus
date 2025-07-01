def PReLU(x, init=0.001, name='output'):
    """
    Parameterized ReLU as in the paper `Delving Deep into Rectifiers: Surpassing
    Human-Level Performance on ImageNet Classification
    <http://arxiv.org/abs/1502.01852>`_.

    Args:
        x (tf.Tensor): input
        init (float): initial value for the learnable slope.
        name (str): name of the output.

    Variable Names:

    * ``alpha``: learnable slope.
    """
    init = tfv1.constant_initializer(init)
    alpha = tfv1.get_variable('alpha', [], initializer=init)
    x = ((1 + alpha) * x + (1 - alpha) * tf.abs(x))
    ret = tf.multiply(x, 0.5, name=name)

    ret.variables = VariableHolder(alpha=alpha)
    return ret