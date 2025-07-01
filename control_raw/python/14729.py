def delete(self):
        """Delete this cluster.

        For example:

        .. literalinclude:: snippets.py
            :start-after: [START bigtable_delete_cluster]
            :end-before: [END bigtable_delete_cluster]

        Marks a cluster and all of its tables for permanent deletion in 7 days.

        Immediately upon completion of the request:

        * Billing will cease for all of the cluster's reserved resources.
        * The cluster's ``delete_time`` field will be set 7 days in the future.

        Soon afterward:

        * All tables within the cluster will become unavailable.

        At the cluster's ``delete_time``:

        * The cluster and **all of its tables** will immediately and
          irrevocably disappear from the API, and their data will be
          permanently deleted.
        """
        client = self._instance._client
        client.instance_admin_client.delete_cluster(self.name)