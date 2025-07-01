def open(self, using=None, **kwargs):
        """
        Opens the index in elasticsearch.

        Any additional keyword arguments will be passed to
        ``Elasticsearch.indices.open`` unchanged.
        """
        return self._get_connection(using).indices.open(index=self._name, **kwargs)