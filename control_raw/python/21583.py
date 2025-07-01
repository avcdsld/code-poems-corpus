def get_upgrade(self, index=None, params=None):
        """
        Monitor how much of one or more index is upgraded.
        `<http://www.elastic.co/guide/en/elasticsearch/reference/current/indices-upgrade.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open', valid
            choices are: 'open', 'closed', 'none', 'all'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        """
        return self.transport.perform_request(
            "GET", _make_path(index, "_upgrade"), params=params
        )