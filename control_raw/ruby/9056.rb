def begin_suspend(resource_group_name, server_name, custom_headers:nil)
      response = begin_suspend_async(resource_group_name, server_name, custom_headers:custom_headers).value!
      nil
    end