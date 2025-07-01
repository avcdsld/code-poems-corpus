def score(self, testing_features, testing_target):
        """Return the score on the given testing data using the user-specified scoring function.

        Parameters
        ----------
        testing_features: array-like {n_samples, n_features}
            Feature matrix of the testing set
        testing_target: array-like {n_samples}
            List of class labels for prediction in the testing set

        Returns
        -------
        accuracy_score: float
            The estimated test set accuracy

        """
        if self.fitted_pipeline_ is None:
            raise RuntimeError('A pipeline has not yet been optimized. Please call fit() first.')

        testing_features, testing_target = self._check_dataset(testing_features, testing_target, sample_weight=None)

        # If the scoring function is a string, we must adjust to use the sklearn
        # scoring interface
        score = SCORERS[self.scoring_function](
            self.fitted_pipeline_,
            testing_features.astype(np.float64),
            testing_target.astype(np.float64)
        )
        return score