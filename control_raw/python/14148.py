def _fill_from_default(self, default_job_config):
        """Merge this job config with a default job config.

        The keys in this object take precedence over the keys in the default
        config. The merge is done at the top-level as well as for keys one
        level below the job type.

        Arguments:
            default_job_config (google.cloud.bigquery.job._JobConfig):
                The default job config that will be used to fill in self.

        Returns:
            google.cloud.bigquery.job._JobConfig A new (merged) job config.
        """
        if self._job_type != default_job_config._job_type:
            raise TypeError(
                "attempted to merge two incompatible job types: "
                + repr(self._job_type)
                + ", "
                + repr(default_job_config._job_type)
            )

        new_job_config = self.__class__()

        default_job_properties = copy.deepcopy(default_job_config._properties)
        for key in self._properties:
            if key != self._job_type:
                default_job_properties[key] = self._properties[key]

        default_job_properties[self._job_type].update(self._properties[self._job_type])
        new_job_config._properties = default_job_properties

        return new_job_config