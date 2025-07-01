def cancel(resource_group_name, vm_scale_set_name, custom_headers:nil)
      response = cancel_async(resource_group_name, vm_scale_set_name, custom_headers:custom_headers).value!
      nil
    end