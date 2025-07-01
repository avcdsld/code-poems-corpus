def step(self, batch_size, max_norm=None):
        """Makes one step of parameter update. Should be called after
        `fp16_optimizer.backward()`, and outside of `record()` scope.

        Parameters
        ----------
        batch_size : int
            Batch size of data processed. Gradient will be normalized by `1/batch_size`.
            Set this to 1 if you normalized loss manually with `loss = mean(loss)`.
        max_norm : NDArray, optional, default is None
            max value for global 2-norm of gradients.
        """
        self.fp32_trainer.allreduce_grads()
        step_size = batch_size * self._scaler.loss_scale
        if max_norm:
            norm, ratio, is_finite = grad_global_norm(self.fp32_trainer._params,
                                                      max_norm * self._scaler.loss_scale)
            step_size = ratio * step_size
            if self._support_nan_check:
                self.fp32_trainer.update(step_size)
                overflow = is_finite.asscalar() < 1
            else:
                overflow = not np.isfinite(norm.asscalar())
                if not overflow:
                    self.fp32_trainer.update(step_size)
        else:
            # TODO(haibin) optimize the performance when max_norm is not present
            # sequentially adding isnan/isinf results may be slow
            if self._support_nan_check:
                self.fp32_trainer.update(step_size)
                overflow = self._scaler.has_overflow(self.fp32_trainer._params)
            else:
                overflow = self._scaler.has_overflow(self.fp32_trainer._params)
                if not overflow:
                    self.fp32_trainer.update(step_size)
        # update scale based on overflow information
        self._scaler.update_scale(overflow)