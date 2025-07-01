def hot_threads(self, node_id=None, params=None):
        """
        An API allowing to get the current hot threads on each node in the cluster.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-hot-threads.html>`_

        :arg node_id: A comma-separated list of node IDs or names to limit the
            returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes
        :arg type: The type to sample (default: cpu), valid choices are:
            'cpu', 'wait', 'block'
        :arg ignore_idle_threads: Don't show threads that are in known-idle
            places, such as waiting on a socket select or pulling from an empty
            task queue (default: true)
        :arg interval: The interval for the second sampling of threads
        :arg snapshots: Number of samples of thread stacktrace (default: 10)
        :arg threads: Specify the number of threads to provide information for
            (default: 3)
        :arg timeout: Explicit operation timeout
        """
        # avoid python reserved words
        if params and "type_" in params:
            params["type"] = params.pop("type_")
        return self.transport.perform_request(
            "GET", _make_path("_cluster", "nodes", node_id, "hotthreads"), params=params
        )