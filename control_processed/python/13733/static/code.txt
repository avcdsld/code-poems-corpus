def _check_dataset(self, features, target, sample_weight=None):
        """Check if a dataset has a valid feature set and labels.

        Parameters
        ----------
        features: array-like {n_samples, n_features}
            Feature matrix
        target: array-like {n_samples} or None
            List of class labels for prediction
        sample_weight: array-like {n_samples} (optional)
            List of weights indicating relative importance
        Returns
        -------
        (features, target)
        """
        # Check sample_weight
        if sample_weight is not None:
            try: sample_weight = np.array(sample_weight).astype('float')
            except ValueError as e:
                raise ValueError('sample_weight could not be converted to float array: %s' % e)
            if np.any(np.isnan(sample_weight)):
                raise ValueError('sample_weight contained NaN values.')
            try: check_consistent_length(sample_weight, target)
            except ValueError as e:
                raise ValueError('sample_weight dimensions did not match target: %s' % e)

        # If features is a sparse matrix, do not apply imputation
        if sparse.issparse(features):
            if self.config_dict in [None, "TPOT light", "TPOT MDR"]:
                raise ValueError(
                    'Not all operators in {} supports sparse matrix. '
                    'Please use \"TPOT sparse\" for sparse matrix.'.format(self.config_dict)
                )
            elif self.config_dict != "TPOT sparse":
                print(
                    'Warning: Since the input matrix is a sparse matrix, please makes sure all the operators in the '
                    'customized config dictionary supports sparse matriies.'
                )
        else:
            if isinstance(features, np.ndarray):
                if np.any(np.isnan(features)):
                    self._imputed = True
            elif isinstance(features, DataFrame):
                if features.isnull().values.any():
                    self._imputed = True

            if self._imputed:
                features = self._impute_values(features)

        try:
            if target is not None:
                X, y = check_X_y(features, target, accept_sparse=True, dtype=None)
                if self._imputed:
                    return X, y
                else:
                    return features, target
            else:
                X = check_array(features, accept_sparse=True, dtype=None)
                if self._imputed:
                    return X
                else:
                    return features
        except (AssertionError, ValueError):
            raise ValueError(
                'Error: Input data is not in a valid format. Please confirm '
                'that the input data is scikit-learn compatible. For example, '
                'the features must be a 2-D array and target labels must be a '
                '1-D array.'
            )