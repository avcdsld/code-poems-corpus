def create_with_http_info(resource_group_name, service_name, group_id, uid, custom_headers:nil)
      create_async(resource_group_name, service_name, group_id, uid, custom_headers:custom_headers).value!
    end