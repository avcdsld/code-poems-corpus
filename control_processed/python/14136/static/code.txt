def _set_properties(self, api_response):
        """Update properties from resource in body of ``api_response``

        :type api_response: dict
        :param api_response: response returned from an API call
        """
        cleaned = api_response.copy()
        self._scrub_local_properties(cleaned)

        statistics = cleaned.get("statistics", {})
        if "creationTime" in statistics:
            statistics["creationTime"] = float(statistics["creationTime"])
        if "startTime" in statistics:
            statistics["startTime"] = float(statistics["startTime"])
        if "endTime" in statistics:
            statistics["endTime"] = float(statistics["endTime"])

        self._properties.clear()
        self._properties.update(cleaned)
        self._copy_configuration_properties(cleaned.get("configuration", {}))

        # For Future interface
        self._set_future_result()