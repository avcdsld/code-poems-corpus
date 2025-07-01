def stop_trial(self, trial, error=False, error_msg=None, stop_logger=True):
        """Only returns resources if resources allocated."""
        prior_status = trial.status
        self._stop_trial(
            trial, error=error, error_msg=error_msg, stop_logger=stop_logger)
        if prior_status == Trial.RUNNING:
            logger.debug("Returning resources for Trial %s.", str(trial))
            self._return_resources(trial.resources)
            out = self._find_item(self._running, trial)
            for result_id in out:
                self._running.pop(result_id)