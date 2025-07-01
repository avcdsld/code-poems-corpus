def clear_cached_roles(self, name, params=None):
        """
        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-clear-role-cache.html>`_

        :arg name: Role name
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")
        return self.transport.perform_request(
            "POST", _make_path("_security", "role", name, "_clear_cache"), params=params
        )