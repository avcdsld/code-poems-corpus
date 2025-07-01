def restart(resource_group_name, vm_name, custom_headers:nil)
      response = restart_async(resource_group_name, vm_name, custom_headers:custom_headers).value!
      nil
    end