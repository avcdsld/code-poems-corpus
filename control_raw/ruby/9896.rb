def list_by_volume_container_with_http_info(device_name, volume_container_name, resource_group_name, manager_name, custom_headers:nil)
      list_by_volume_container_async(device_name, volume_container_name, resource_group_name, manager_name, custom_headers:custom_headers).value!
    end