def begin_list_routes_table_with_http_info(resource_group_name, circuit_name, peering_name, device_path, custom_headers:nil)
      begin_list_routes_table_async(resource_group_name, circuit_name, peering_name, device_path, custom_headers:custom_headers).value!
    end