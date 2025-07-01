def stop_trial(self, trial_id):
        """Requests to stop trial by trial_id."""
        response = requests.put(
            urljoin(self._path, "trials/{}".format(trial_id)))
        return self._deserialize(response)