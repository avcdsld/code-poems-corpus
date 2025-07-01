def put_mapping(self, using=None, **kwargs):
        """
        Register specific mapping definition for a specific type.

        Any additional keyword arguments will be passed to
        ``Elasticsearch.indices.put_mapping`` unchanged.
        """
        return self._get_connection(using).indices.put_mapping(index=self._name, **kwargs)