def start(resource_group_name, container_group_name, custom_headers:nil)
      response = start_async(resource_group_name, container_group_name, custom_headers:custom_headers).value!
      nil
    end