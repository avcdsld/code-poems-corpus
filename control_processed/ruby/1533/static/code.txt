def create_read_replica(options = {})
      options = options.merge(source_db_instance_identifier: @id)
      resp = @client.create_db_instance_read_replica(options)
      DBInstance.new(
        id: resp.data.db_instance.db_instance_identifier,
        data: resp.data.db_instance,
        client: @client
      )
    end