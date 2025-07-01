def begin_delete_with_http_info(fabric_name, network_name, network_mapping_name, custom_headers:nil)
      begin_delete_async(fabric_name, network_name, network_mapping_name, custom_headers:custom_headers).value!
    end