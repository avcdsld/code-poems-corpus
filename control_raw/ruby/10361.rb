def begin_restart(resource_group_name, vm_name, custom_headers:nil)
      response = begin_restart_async(resource_group_name, vm_name, custom_headers:custom_headers).value!
      nil
    end