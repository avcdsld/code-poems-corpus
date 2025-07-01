def update(resource_group_name, vm_name, vm_extension_name, extension_parameters, custom_headers:nil)
      response = update_async(resource_group_name, vm_name, vm_extension_name, extension_parameters, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end