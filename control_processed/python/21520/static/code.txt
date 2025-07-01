def delete_watch(self, id, params=None):
        """
        `<http://www.elastic.co/guide/en/elasticsearch/reference/current/watcher-api-delete-watch.html>`_

        :arg id: Watch ID
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")
        return self.transport.perform_request(
            "DELETE", _make_path("_watcher", "watch", id), params=params
        )