def begin_reset_shared_key_with_http_info(resource_group_name, virtual_network_gateway_connection_name, parameters, custom_headers:nil)
      begin_reset_shared_key_async(resource_group_name, virtual_network_gateway_connection_name, parameters, custom_headers:custom_headers).value!
    end