def delete(resource_group_name, network_interface_name, tap_configuration_name, custom_headers:nil)
      response = delete_async(resource_group_name, network_interface_name, tap_configuration_name, custom_headers:custom_headers).value!
      nil
    end