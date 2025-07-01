def analyze(self, using=None, **kwargs):
        """
        Perform the analysis process on a text and return the tokens breakdown
        of the text.

        Any additional keyword arguments will be passed to
        ``Elasticsearch.indices.analyze`` unchanged.
        """
        return self._get_connection(using).indices.analyze(index=self._name, **kwargs)