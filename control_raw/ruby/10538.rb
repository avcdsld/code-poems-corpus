def delete(resource_group_name, appliance_name, custom_headers:nil)
      response = delete_async(resource_group_name, appliance_name, custom_headers:custom_headers).value!
      nil
    end