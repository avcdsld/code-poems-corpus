def open(self, target_uri, **kwargs):
        """Open target uri.

        :param target_uri: Uri to open
        :type target_uri: string

        :returns: Target object

        """
        target = urlsplit(target_uri, scheme=self.default_opener)

        opener = self.get_opener(target.scheme)
        query = opener.conform_query(target.query)

        target = opener.get_target(
            target.scheme,
            target.path,
            target.fragment,
            target.username,
            target.password,
            target.hostname,
            target.port,
            query,
            **kwargs
        )
        target.opener_path = target_uri

        return target