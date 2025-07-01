def get_settings(self, using=None, **kwargs):
        """
        Retrieve settings for the index.

        Any additional keyword arguments will be passed to
        ``Elasticsearch.indices.get_settings`` unchanged.
        """
        return self._get_connection(using).indices.get_settings(index=self._name, **kwargs)