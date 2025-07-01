def list_by_database(resource_group_name, cluster_name, database_name, custom_headers:nil)
      response = list_by_database_async(resource_group_name, cluster_name, database_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end