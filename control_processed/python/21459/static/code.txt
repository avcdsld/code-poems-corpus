def add_connection(self, host):
        """
        Create a new :class:`~elasticsearch.Connection` instance and add it to the pool.

        :arg host: kwargs that will be used to create the instance
        """
        self.hosts.append(host)
        self.set_connections(self.hosts)