def list_clusters(self):
        """List the clusters in this instance.

        For example:

        .. literalinclude:: snippets.py
            :start-after: [START bigtable_list_clusters_on_instance]
            :end-before: [END bigtable_list_clusters_on_instance]

        :rtype: tuple
        :returns:
            (clusters, failed_locations), where 'clusters' is list of
            :class:`google.cloud.bigtable.instance.Cluster`, and
            'failed_locations' is a list of locations which could not
            be resolved.
        """
        resp = self._client.instance_admin_client.list_clusters(self.name)
        clusters = [Cluster.from_pb(cluster, self) for cluster in resp.clusters]
        return clusters, resp.failed_locations