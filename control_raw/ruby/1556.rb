def create_snapshot(options = {})
      options = options.merge(db_cluster_identifier: @id)
      resp = @client.create_db_cluster_snapshot(options)
      DBClusterSnapshot.new(
        cluster_id: resp.data.db_cluster_snapshot.db_cluster_identifier,
        snapshot_id: resp.data.db_cluster_snapshot.db_cluster_snapshot_identifier,
        data: resp.data.db_cluster_snapshot,
        client: @client
      )
    end