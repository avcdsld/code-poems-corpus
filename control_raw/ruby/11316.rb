def begin_acquire_with_http_info(resource_group_name, server_name, dns_alias_name, parameters, custom_headers:nil)
      begin_acquire_async(resource_group_name, server_name, dns_alias_name, parameters, custom_headers:custom_headers).value!
    end