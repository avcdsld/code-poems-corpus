def get_supported_methods(self, url):
        """Get a list of supported methods for a url and optional host.

        :param url: URL string (including host)
        :return: frozenset of supported methods
        """
        route = self.routes_all.get(url)
        # if methods are None then this logic will prevent an error
        return getattr(route, "methods", None) or frozenset()