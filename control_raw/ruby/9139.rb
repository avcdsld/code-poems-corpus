def begin_update_policies(resource_group_name, registry_name, registry_policies_update_parameters, custom_headers:nil)
      response = begin_update_policies_async(resource_group_name, registry_name, registry_policies_update_parameters, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end