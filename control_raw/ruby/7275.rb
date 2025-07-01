def begin_update_tags_with_http_info(resource_group_name, virtual_network_gateway_name, parameters, custom_headers:nil)
      begin_update_tags_async(resource_group_name, virtual_network_gateway_name, parameters, custom_headers:custom_headers).value!
    end