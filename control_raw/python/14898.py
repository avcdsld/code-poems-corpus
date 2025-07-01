def log_text(self, text, client=None, **kw):
        """API call:  log a text message via a POST request

        See
        https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write

        :type text: str
        :param text: the log message.

        :type client: :class:`~google.cloud.logging.client.Client` or
                      ``NoneType``
        :param client: the client to use.  If not passed, falls back to the
                       ``client`` stored on the current logger.

        :type kw: dict
        :param kw: (optional) additional keyword arguments for the entry.
                   See :class:`~google.cloud.logging.entries.LogEntry`.
        """
        self._do_log(client, TextEntry, text, **kw)