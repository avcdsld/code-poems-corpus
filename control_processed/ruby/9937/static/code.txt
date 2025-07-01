def list_supported_configurations(resource_group_name, manager_name, custom_headers:nil)
      response = list_supported_configurations_async(resource_group_name, manager_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end