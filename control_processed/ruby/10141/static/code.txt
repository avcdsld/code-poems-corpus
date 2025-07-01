def begin_update(resource_group_name, private_zone_name, virtual_network_link_name, parameters, if_match:nil, custom_headers:nil)
      response = begin_update_async(resource_group_name, private_zone_name, virtual_network_link_name, parameters, if_match:if_match, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end