def start_osupgrade(resource_group_name, vm_scale_set_name, custom_headers:nil)
      response = start_osupgrade_async(resource_group_name, vm_scale_set_name, custom_headers:custom_headers).value!
      nil
    end