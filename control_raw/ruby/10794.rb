def begin_delete_with_http_info(resource_group_name, managed_instance_name, database_name, custom_headers:nil)
      begin_delete_async(resource_group_name, managed_instance_name, database_name, custom_headers:custom_headers).value!
    end