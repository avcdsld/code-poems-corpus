def get_global(self):
        """Gets the current global evaluation result.

        Returns
        -------
        names : list of str
           Name of the metrics.
        values : list of float
           Value of the evaluations.
        """
        if self._has_global_stats:
            if self.global_num_inst == 0:
                return (self.name, float('nan'))
            else:
                return (self.name, self.global_sum_metric / self.global_num_inst)
        else:
            return self.get()