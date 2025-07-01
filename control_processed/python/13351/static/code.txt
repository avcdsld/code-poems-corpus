def fit(self, validation_data=None, **kwargs):
        """
        Args:
            validation_data (DataFlow or InputSource): to be used for inference.
                The inference callback is added as the first in the callback list.
                If you need to use it in a different order, please write it in the callback list manually.
            kwargs: same arguments as :meth:`Trainer.train_with_defaults`.
        """
        callbacks = kwargs.pop('callbacks', [])
        if validation_data is not None:
            # There is no way to guess where users want this callback. So we have to choose one.
            # MinSaver may need results from this callback,
            # so we put this callback at first.
            callbacks.insert(0, InferenceRunner(
                validation_data, ScalarStats(self._stats_to_inference)))
        self.trainer.train_with_defaults(callbacks=callbacks, **kwargs)