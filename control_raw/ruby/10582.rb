def begin_refresh(device_name, name, resource_group_name, custom_headers:nil)
      response = begin_refresh_async(device_name, name, resource_group_name, custom_headers:custom_headers).value!
      nil
    end