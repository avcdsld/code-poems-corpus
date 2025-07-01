def _write_max_gradient(self)->None:
        "Writes the maximum of the gradients to Tensorboard."
        max_gradient = max(x.data.max() for x in self.gradients)
        self._add_gradient_scalar('max_gradient', scalar_value=max_gradient)