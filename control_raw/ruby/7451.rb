def begin_perform_maintenance_with_http_info(resource_group_name, vm_scale_set_name, vm_instance_ids:nil, custom_headers:nil)
      begin_perform_maintenance_async(resource_group_name, vm_scale_set_name, vm_instance_ids:vm_instance_ids, custom_headers:custom_headers).value!
    end