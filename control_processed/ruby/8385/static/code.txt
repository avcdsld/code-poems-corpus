def begin_update_security_settings(device_name, parameters, resource_group_name, manager_name, custom_headers:nil)
      response = begin_update_security_settings_async(device_name, parameters, resource_group_name, manager_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end