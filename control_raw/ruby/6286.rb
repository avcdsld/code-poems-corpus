def begin_delete(resource_group_name, circuit_name, custom_headers:nil)
      response = begin_delete_async(resource_group_name, circuit_name, custom_headers:custom_headers).value!
      nil
    end