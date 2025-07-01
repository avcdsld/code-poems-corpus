def invalidate_api_key(self, body, params=None):
        """
        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-invalidate-api-key.html>`_

        :arg body: The api key request to invalidate API key(s)
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")
        return self.transport.perform_request(
            "DELETE", "/_security/api_key", params=params, body=body
        )