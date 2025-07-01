def fit(self, X, y, group, sample_weight=None, eval_set=None, sample_weight_eval_set=None,
            eval_group=None, eval_metric=None, early_stopping_rounds=None,
            verbose=False, xgb_model=None, callbacks=None):
        # pylint: disable = attribute-defined-outside-init,arguments-differ
        """
        Fit the gradient boosting model

        Parameters
        ----------
        X : array_like
            Feature matrix
        y : array_like
            Labels
        group : array_like
            group size of training data
        sample_weight : array_like
            group weights

            .. note:: Weights are per-group for ranking tasks

                In ranking task, one weight is assigned to each group (not each data
                point). This is because we only care about the relative ordering of
                data points within each group, so it doesn't make sense to assign
                weights to individual data points.

        eval_set : list, optional
            A list of (X, y) tuple pairs to use as a validation set for
            early-stopping
        sample_weight_eval_set : list, optional
            A list of the form [L_1, L_2, ..., L_n], where each L_i is a list of
            group weights on the i-th validation set.

            .. note:: Weights are per-group for ranking tasks

                In ranking task, one weight is assigned to each group (not each data
                point). This is because we only care about the relative ordering of
                data points within each group, so it doesn't make sense to assign
                weights to individual data points.

        eval_group : list of arrays, optional
            A list that contains the group size corresponds to each
            (X, y) pair in eval_set
        eval_metric : str, callable, optional
            If a str, should be a built-in evaluation metric to use. See
            doc/parameter.rst. If callable, a custom evaluation metric. The call
            signature is func(y_predicted, y_true) where y_true will be a
            DMatrix object such that you may need to call the get_label
            method. It must return a str, value pair where the str is a name
            for the evaluation and value is the value of the evaluation
            function. This objective is always minimized.
        early_stopping_rounds : int
            Activates early stopping. Validation error needs to decrease at
            least every <early_stopping_rounds> round(s) to continue training.
            Requires at least one item in evals.  If there's more than one,
            will use the last. Returns the model from the last iteration
            (not the best one). If early stopping occurs, the model will
            have three additional fields: bst.best_score, bst.best_iteration
            and bst.best_ntree_limit.
            (Use bst.best_ntree_limit to get the correct value if num_parallel_tree
            and/or num_class appears in the parameters)
        verbose : bool
            If `verbose` and an evaluation set is used, writes the evaluation
            metric measured on the validation set to stderr.
        xgb_model : str
            file name of stored xgb model or 'Booster' instance Xgb model to be
            loaded before training (allows training continuation).
        callbacks : list of callback functions
            List of callback functions that are applied at end of each iteration.
            It is possible to use predefined callbacks by using :ref:`callback_api`.
            Example:

            .. code-block:: python

                [xgb.callback.reset_learning_rate(custom_rates)]
        """
        # check if group information is provided
        if group is None:
            raise ValueError("group is required for ranking task")

        if eval_set is not None:
            if eval_group is None:
                raise ValueError("eval_group is required if eval_set is not None")
            if len(eval_group) != len(eval_set):
                raise ValueError("length of eval_group should match that of eval_set")
            if any(group is None for group in eval_group):
                raise ValueError("group is required for all eval datasets for ranking task")

        def _dmat_init(group, **params):
            ret = DMatrix(**params)
            ret.set_group(group)
            return ret

        if sample_weight is not None:
            train_dmatrix = _dmat_init(group, data=X, label=y, weight=sample_weight,
                                       missing=self.missing, nthread=self.n_jobs)
        else:
            train_dmatrix = _dmat_init(group, data=X, label=y,
                                       missing=self.missing, nthread=self.n_jobs)

        evals_result = {}

        if eval_set is not None:
            if sample_weight_eval_set is None:
                sample_weight_eval_set = [None] * len(eval_set)
            evals = [_dmat_init(eval_group[i], data=eval_set[i][0], label=eval_set[i][1],
                                missing=self.missing, weight=sample_weight_eval_set[i],
                                nthread=self.n_jobs) for i in range(len(eval_set))]
            nevals = len(evals)
            eval_names = ["eval_{}".format(i) for i in range(nevals)]
            evals = list(zip(evals, eval_names))
        else:
            evals = ()

        params = self.get_xgb_params()

        feval = eval_metric if callable(eval_metric) else None
        if eval_metric is not None:
            if callable(eval_metric):
                eval_metric = None
            else:
                params.update({'eval_metric': eval_metric})

        self._Booster = train(params, train_dmatrix,
                              self.n_estimators,
                              early_stopping_rounds=early_stopping_rounds, evals=evals,
                              evals_result=evals_result, feval=feval,
                              verbose_eval=verbose, xgb_model=xgb_model,
                              callbacks=callbacks)

        self.objective = params["objective"]

        if evals_result:
            for val in evals_result.items():
                evals_result_key = list(val[1].keys())[0]
                evals_result[val[0]][evals_result_key] = val[1][evals_result_key]
            self.evals_result = evals_result

        if early_stopping_rounds is not None:
            self.best_score = self._Booster.best_score
            self.best_iteration = self._Booster.best_iteration
            self.best_ntree_limit = self._Booster.best_ntree_limit

        return self