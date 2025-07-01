def begin_delete_with_http_info(fabric_name, protection_container_name, mapping_name, removal_input, custom_headers:nil)
      begin_delete_async(fabric_name, protection_container_name, mapping_name, removal_input, custom_headers:custom_headers).value!
    end