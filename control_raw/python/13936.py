def iter(self, headers_only=False, page_size=None):
        """Yield all time series objects selected by the query.

        The generator returned iterates over
        :class:`~google.cloud.monitoring_v3.types.TimeSeries` objects
        containing points ordered from oldest to newest.

        Note that the :class:`Query` object itself is an iterable, such that
        the following are equivalent::

            for timeseries in query:
                ...

            for timeseries in query.iter():
                ...

        :type headers_only: bool
        :param headers_only:
             Whether to omit the point data from the time series objects.

        :type page_size: int
        :param page_size:
            (Optional) The maximum number of points in each page of results
            from this request. Non-positive values are ignored. Defaults
            to a sensible value set by the API.

        :raises: :exc:`ValueError` if the query time interval has not been
            specified.
        """
        if self._end_time is None:
            raise ValueError("Query time interval not specified.")

        params = self._build_query_params(headers_only, page_size)
        for ts in self._client.list_time_series(**params):
            yield ts