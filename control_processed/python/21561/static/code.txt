def update_datafeed(self, datafeed_id, body, params=None):
        """
        `<http://www.elastic.co/guide/en/elasticsearch/reference/current/ml-update-datafeed.html>`_

        :arg datafeed_id: The ID of the datafeed to update
        :arg body: The datafeed update settings
        """
        for param in (datafeed_id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")
        return self.transport.perform_request(
            "POST",
            _make_path("_ml", "datafeeds", datafeed_id, "_update"),
            params=params,
            body=body,
        )