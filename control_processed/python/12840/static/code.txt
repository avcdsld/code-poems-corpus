def predict(self, train_x):
        """Predict the result.
        Args:
            train_x: A list of NetworkDescriptor.
        Returns:
            y_mean: The predicted mean.
            y_std: The predicted standard deviation.
        """
        k_trans = np.exp(-np.power(edit_distance_matrix(train_x, self._x), 2))
        y_mean = k_trans.dot(self._alpha_vector)  # Line 4 (y_mean = f_star)

        # compute inverse K_inv of K based on its Cholesky
        # decomposition L and its inverse L_inv
        l_inv = solve_triangular(self._l_matrix.T, np.eye(self._l_matrix.shape[0]))
        k_inv = l_inv.dot(l_inv.T)
        # Compute variance of predictive distribution
        y_var = np.ones(len(train_x), dtype=np.float)
        y_var -= np.einsum("ij,ij->i", np.dot(k_trans, k_inv), k_trans)

        # Check if any of the variances is negative because of
        # numerical issues. If yes: set the variance to 0.
        y_var_negative = y_var < 0
        if np.any(y_var_negative):
            y_var[y_var_negative] = 0.0
        return y_mean, np.sqrt(y_var)