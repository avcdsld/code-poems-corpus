def _build_train_op(self):
        """Build training specific ops for the graph."""
        num_gpus = self.hps.num_gpus if self.hps.num_gpus != 0 else 1
        # The learning rate schedule is dependent on the number of gpus.
        boundaries = [int(20000 * i / np.sqrt(num_gpus)) for i in range(2, 5)]
        values = [0.1, 0.01, 0.001, 0.0001]
        self.lrn_rate = tf.train.piecewise_constant(self.global_step,
                                                    boundaries, values)
        tf.summary.scalar("learning rate", self.lrn_rate)

        if self.hps.optimizer == "sgd":
            optimizer = tf.train.GradientDescentOptimizer(self.lrn_rate)
        elif self.hps.optimizer == "mom":
            optimizer = tf.train.MomentumOptimizer(self.lrn_rate, 0.9)

        apply_op = optimizer.minimize(self.cost, global_step=self.global_step)
        train_ops = [apply_op] + self._extra_train_ops
        self.train_op = tf.group(*train_ops)
        self.variables = ray.experimental.tf_utils.TensorFlowVariables(
            self.train_op)