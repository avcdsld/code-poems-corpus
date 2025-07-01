def _http(self):
        """Getter for object used for HTTP transport.

        :rtype: :class:`~requests.Session`
        :returns: An HTTP object.
        """
        if self._http_internal is None:
            self._http_internal = google.auth.transport.requests.AuthorizedSession(
                self._credentials
            )
        return self._http_internal