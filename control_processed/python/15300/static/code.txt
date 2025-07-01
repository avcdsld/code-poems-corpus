def create_projected_dual(self):
    """Function to create variables for the projected dual object.
    Function that projects the input dual variables onto the feasible set.
    Returns:
      projected_dual: Feasible dual solution corresponding to current dual
    """
    # TODO: consider whether we can use shallow copy of the lists without
    # using tf.identity
    projected_nu = tf.placeholder(tf.float32, shape=[])
    min_eig_h = tf.placeholder(tf.float32, shape=[])
    projected_lambda_pos = [tf.identity(x) for x in self.lambda_pos]
    projected_lambda_neg = [tf.identity(x) for x in self.lambda_neg]
    projected_lambda_quad = [
        tf.identity(x) for x in self.lambda_quad
    ]
    projected_lambda_lu = [tf.identity(x) for x in self.lambda_lu]

    for i in range(self.nn_params.num_hidden_layers + 1):
      # Making H PSD
      projected_lambda_lu[i] = self.lambda_lu[i] + 0.5*tf.maximum(-min_eig_h, 0) + TOL
      # Adjusting the value of \lambda_neg to make change in g small
      projected_lambda_neg[i] = self.lambda_neg[i] + tf.multiply(
          (self.lower[i] + self.upper[i]),
          (self.lambda_lu[i] - projected_lambda_lu[i]))
      projected_lambda_neg[i] = (tf.multiply(self.negative_indices[i],
                                             projected_lambda_neg[i]) +
                                 tf.multiply(self.switch_indices[i],
                                             tf.maximum(projected_lambda_neg[i], 0)))

    projected_dual_var = {
        'lambda_pos': projected_lambda_pos,
        'lambda_neg': projected_lambda_neg,
        'lambda_lu': projected_lambda_lu,
        'lambda_quad': projected_lambda_quad,
        'nu': projected_nu,
    }
    projected_dual_object = DualFormulation(
        self.sess, projected_dual_var, self.nn_params,
        self.test_input, self.true_class,
        self.adv_class, self.input_minval,
        self.input_maxval, self.epsilon,
        self.lzs_params,
        project_dual=False)
    projected_dual_object.min_eig_val_h = min_eig_h
    return projected_dual_object