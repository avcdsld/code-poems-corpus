def generate(self, x, **kwargs):
    """
    Generate symbolic graph for adversarial examples and return.

    :param x: The model's symbolic inputs.
    :param kwargs: See `parse_params`
    """
    # Parse and save attack-specific parameters
    assert self.parse_params(**kwargs)

    if self.symbolic_impl:
      # Create random targets if y_target not provided
      if self.y_target is None:
        from random import randint

        def random_targets(gt):
          result = gt.copy()
          nb_s = gt.shape[0]
          nb_classes = gt.shape[1]

          for i in range(nb_s):
            result[i, :] = np.roll(result[i, :],
                                   randint(1, nb_classes - 1))

          return result

        labels, nb_classes = self.get_or_guess_labels(x, kwargs)
        self.y_target = tf.py_func(random_targets, [labels],
                                   self.tf_dtype)
        self.y_target.set_shape([None, nb_classes])

      x_adv = jsma_symbolic(
          x,
          model=self.model,
          y_target=self.y_target,
          theta=self.theta,
          gamma=self.gamma,
          clip_min=self.clip_min,
          clip_max=self.clip_max)
    else:
      raise NotImplementedError("The jsma_batch function has been removed."
                                " The symbolic_impl argument to SaliencyMapMethod will be removed"
                                " on 2019-07-18 or after. Any code that depends on the non-symbolic"
                                " implementation of the JSMA should be revised. Consider using"
                                " SaliencyMapMethod.generate_np() instead.")

    return x_adv