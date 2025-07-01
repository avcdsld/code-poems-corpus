def allocation_explain(self, body=None, params=None):
        """
        `<http://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-allocation-explain.html>`_

        :arg body: The index, shard, and primary flag to explain. Empty means
            'explain the first unassigned shard'
        :arg include_disk_info: Return information about disk usage and shard
            sizes (default: false)
        :arg include_yes_decisions: Return 'YES' decisions in explanation
            (default: false)
        """
        return self.transport.perform_request('GET',
            '/_cluster/allocation/explain', params=params, body=body)