def regenerate_primary_key_with_http_info(resource_group_name, service_name, sid, custom_headers:nil)
      regenerate_primary_key_async(resource_group_name, service_name, sid, custom_headers:custom_headers).value!
    end