def get_with_http_info(resource_group_name, service_name, sid, custom_headers:nil)
      get_async(resource_group_name, service_name, sid, custom_headers:custom_headers).value!
    end