def begin_start_with_http_info(endpoint_name, profile_name, resource_group_name, custom_headers:nil)
      begin_start_async(endpoint_name, profile_name, resource_group_name, custom_headers:custom_headers).value!
    end