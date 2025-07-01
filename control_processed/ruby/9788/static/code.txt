def list_routes_table_summary(resource_group_name, cross_connection_name, peering_name, device_path, custom_headers:nil)
      response = list_routes_table_summary_async(resource_group_name, cross_connection_name, peering_name, device_path, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end