def begin_update_with_http_info(resource_group_name, server_name, database_name, sync_group_name, sync_member_name, parameters, custom_headers:nil)
      begin_update_async(resource_group_name, server_name, database_name, sync_group_name, sync_member_name, parameters, custom_headers:custom_headers).value!
    end