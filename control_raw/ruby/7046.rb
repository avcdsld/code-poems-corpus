def begin_delete(fabric_name, protection_container_name, mapping_name, removal_input, custom_headers:nil)
      response = begin_delete_async(fabric_name, protection_container_name, mapping_name, removal_input, custom_headers:custom_headers).value!
      nil
    end