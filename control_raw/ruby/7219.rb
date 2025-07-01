def deallocate(resource_group_name, vm_name, custom_headers:nil)
      response = deallocate_async(resource_group_name, vm_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end