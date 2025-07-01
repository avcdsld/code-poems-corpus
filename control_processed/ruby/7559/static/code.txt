def begin_create_or_update_with_http_info(resource_group_name, resource_name, parameters:nil, custom_headers:nil)
      begin_create_or_update_async(resource_group_name, resource_name, parameters:parameters, custom_headers:custom_headers).value!
    end