def create_db_cluster(options = {})
      resp = @client.create_db_cluster(options)
      DBCluster.new(
        id: options[:db_cluster][:db_cluster_identifier],
        data: resp.data.db_cluster,
        client: @client
      )
    end