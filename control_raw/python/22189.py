def hybrid_forward(self, F, x, sampled_values, label, weight, bias):
        """Forward computation."""
        sampled_candidates, _, _ = sampled_values
        # (batch_size,)
        label = F.reshape(label, shape=(-1,))
        # (num_sampled+batch_size,)
        ids = F.concat(sampled_candidates, label, dim=0)
        # lookup weights and biases
        # (num_sampled+batch_size, dim)
        w_all = F.Embedding(data=ids, weight=weight,
                            input_dim=self._num_classes, output_dim=self._in_unit,
                            sparse_grad=self._sparse_grad)
        # (num_sampled+batch_size, 1)
        b_all = F.take(bias, indices=ids)
        return self._dense(x, sampled_values, label, w_all, b_all)