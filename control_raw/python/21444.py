def ping(self, params=None):
        """
        Returns True if the cluster is up, False otherwise.
        `<http://www.elastic.co/guide/>`_
        """
        try:
            return self.transport.perform_request("HEAD", "/", params=params)
        except TransportError:
            return False