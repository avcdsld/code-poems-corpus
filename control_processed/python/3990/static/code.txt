def predict(self, data, output_margin=False, ntree_limit=None, validate_features=True):
        """
        Predict with `data`.

        .. note:: This function is not thread safe.

          For each booster object, predict can only be called from one thread.
          If you want to run prediction using multiple thread, call ``xgb.copy()`` to make copies
          of model object and then call ``predict()``.

        .. note:: Using ``predict()`` with DART booster

          If the booster object is DART type, ``predict()`` will perform dropouts, i.e. only
          some of the trees will be evaluated. This will produce incorrect results if ``data`` is
          not the training data. To obtain correct results on test sets, set ``ntree_limit`` to
          a nonzero value, e.g.

          .. code-block:: python

            preds = bst.predict(dtest, ntree_limit=num_round)

        Parameters
        ----------
        data : DMatrix
            The dmatrix storing the input.
        output_margin : bool
            Whether to output the raw untransformed margin value.
        ntree_limit : int
            Limit number of trees in the prediction; defaults to best_ntree_limit if defined
            (i.e. it has been trained with early stopping), otherwise 0 (use all trees).
        validate_features : bool
            When this is True, validate that the Booster's and data's feature_names are identical.
            Otherwise, it is assumed that the feature_names are the same.
        Returns
        -------
        prediction : numpy array
        """
        test_dmatrix = DMatrix(data, missing=self.missing, nthread=self.n_jobs)
        if ntree_limit is None:
            ntree_limit = getattr(self, "best_ntree_limit", 0)
        class_probs = self.get_booster().predict(test_dmatrix,
                                                 output_margin=output_margin,
                                                 ntree_limit=ntree_limit,
                                                 validate_features=validate_features)
        if output_margin:
            # If output_margin is active, simply return the scores
            return class_probs

        if len(class_probs.shape) > 1:
            column_indexes = np.argmax(class_probs, axis=1)
        else:
            column_indexes = np.repeat(0, class_probs.shape[0])
            column_indexes[class_probs > 0.5] = 1
        return self._le.inverse_transform(column_indexes)