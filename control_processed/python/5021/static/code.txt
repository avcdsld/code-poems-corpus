def set_mode(self, mode):
    """Set hparams with the given mode."""
    log_info("Setting T2TModel mode to '%s'", mode)
    hparams = hparams_lib.copy_hparams(self._original_hparams)
    hparams.add_hparam("mode", mode)
    # When not in training mode, set all forms of dropout to zero.
    if mode != tf.estimator.ModeKeys.TRAIN:
      for key in hparams.values():
        if key.endswith("dropout") or key == "label_smoothing":
          log_info("Setting hparams.%s to 0.0", key)
          setattr(hparams, key, 0.0)
    self._hparams = hparams