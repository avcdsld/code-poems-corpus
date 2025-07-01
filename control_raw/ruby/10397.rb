def begin_delete_with_http_info(resource_group_name, hub_name, relationship_name, custom_headers:nil)
      begin_delete_async(resource_group_name, hub_name, relationship_name, custom_headers:custom_headers).value!
    end