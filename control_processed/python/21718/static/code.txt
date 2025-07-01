def configure(self, **kwargs):
        """
        Configure multiple connections at once, useful for passing in config
        dictionaries obtained from other sources, like Django's settings or a
        configuration management tool.

        Example::

            connections.configure(
                default={'hosts': 'localhost'},
                dev={'hosts': ['esdev1.example.com:9200'], sniff_on_start=True}
            )

        Connections will only be constructed lazily when requested through
        ``get_connection``.
        """
        for k in list(self._conns):
            # try and preserve existing client to keep the persistent connections alive
            if k in self._kwargs and kwargs.get(k, None) == self._kwargs[k]:
                continue
            del self._conns[k]
        self._kwargs = kwargs