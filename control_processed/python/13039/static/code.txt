def handle_initialize(self, data):
        """Initialize Tuner, including creating Bayesian optimization-based parametric models 
        and search space formations

        Parameters
        ----------
        data: search space
            search space of this experiment

        Raises
        ------
        ValueError
            Error: Search space is None
        """
        logger.info('start to handle_initialize')
        # convert search space jason to ConfigSpace
        self.handle_update_search_space(data)

        # generate BOHB config_generator using Bayesian optimization
        if self.search_space:
            self.cg = CG_BOHB(configspace=self.search_space,
                              min_points_in_model=self.min_points_in_model,
                              top_n_percent=self.top_n_percent,
                              num_samples=self.num_samples,
                              random_fraction=self.random_fraction,
                              bandwidth_factor=self.bandwidth_factor,
                              min_bandwidth=self.min_bandwidth)
        else:
            raise ValueError('Error: Search space is None')
        # generate first brackets
        self.generate_new_bracket()
        send(CommandType.Initialized, '')