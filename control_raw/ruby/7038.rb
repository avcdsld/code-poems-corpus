def update(fabric_name, protection_container_name, mapping_name, update_input, custom_headers:nil)
      response = update_async(fabric_name, protection_container_name, mapping_name, update_input, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end