def begin_failover_allow_data_loss(resource_group_name, server_name, database_name, link_id, custom_headers:nil)
      response = begin_failover_allow_data_loss_async(resource_group_name, server_name, database_name, link_id, custom_headers:custom_headers).value!
      nil
    end