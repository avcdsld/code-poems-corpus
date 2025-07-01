def begin_get_advertised_routes(resource_group_name, virtual_network_gateway_name, peer, custom_headers:nil)
      response = begin_get_advertised_routes_async(resource_group_name, virtual_network_gateway_name, peer, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end