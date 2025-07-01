def begin_reset_with_http_info(resource_group_name, virtual_network_gateway_name, gateway_vip:nil, custom_headers:nil)
      begin_reset_async(resource_group_name, virtual_network_gateway_name, gateway_vip:gateway_vip, custom_headers:custom_headers).value!
    end