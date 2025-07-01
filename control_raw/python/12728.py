def generate_parameters(self, parameter_id):
        """
        Returns a set of trial (hyper-)parameters, as a serializable object.

        Parameters
        ----------
        parameter_id : int

        Returns
        -------
        params : dict
        """
        total_params = self.get_suggestion(random_search=False)
        # avoid generating same parameter with concurrent trials because hyperopt doesn't support parallel mode
        if total_params in self.total_data.values():
            # but it can cause deplicate parameter rarely
            total_params = self.get_suggestion(random_search=True)
        self.total_data[parameter_id] = total_params
        params = _split_index(total_params)
        return params