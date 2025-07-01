def begin_convert_to_managed_disks(resource_group_name, vm_name, custom_headers:nil)
      response = begin_convert_to_managed_disks_async(resource_group_name, vm_name, custom_headers:custom_headers).value!
      nil
    end