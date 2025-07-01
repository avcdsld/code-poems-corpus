def thread_pool(self, thread_pool_patterns=None, params=None):
        """
        Get information about thread pools.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-thread-pool.html>`_

        :arg thread_pool_patterns: A comma-separated list of regular-expressions
            to filter the thread pools in the output
        :arg format: a short version of the Accept header, e.g. json, yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg s: Comma-separated list of column names or column aliases to sort
            by
        :arg size: The multiplier in which to display values, valid choices are:
            '', 'k', 'm', 'g', 't', 'p'
        :arg v: Verbose mode. Display column headers, default False
        """
        return self.transport.perform_request('GET', _make_path('_cat',
            'thread_pool', thread_pool_patterns), params=params)