def list_by_user_with_http_info(resource_group_name, service_name, filter, top:nil, skip:nil, custom_headers:nil)
      list_by_user_async(resource_group_name, service_name, filter, top:top, skip:skip, custom_headers:custom_headers).value!
    end