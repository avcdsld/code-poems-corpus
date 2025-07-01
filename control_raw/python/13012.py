def predict(self, trial_history):
        """predict the value of target position
        
        Parameters
        ----------
        trial_history: list
            The history performance matrix of each trial.

        Returns
        -------
        float
            expected final result performance of this hyperparameter config
        """
        self.trial_history = trial_history
        self.point_num = len(trial_history)
        self.fit_theta()
        self.filter_curve()
        if self.effective_model_num < LEAST_FITTED_FUNCTION:
            # different curve's predictions are too scattered, requires more information
            return None
        self.mcmc_sampling()
        ret = 0
        for i in range(NUM_OF_INSTANCE):
            ret += self.f_comb(self.target_pos, self.weight_samples[i])
        return ret / NUM_OF_INSTANCE