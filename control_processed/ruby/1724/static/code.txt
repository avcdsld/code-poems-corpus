def copy(options = {})
      options = options.merge(source_db_snapshot_identifier: @snapshot_id)
      resp = @client.copy_db_snapshot(options)
      DBSnapshot.new(
        instance_id: resp.data.db_snapshot.db_instance_identifier,
        snapshot_id: resp.data.db_snapshot.db_snapshot_identifier,
        data: resp.data.db_snapshot,
        client: @client
      )
    end