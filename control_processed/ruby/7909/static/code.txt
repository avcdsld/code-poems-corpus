def remove(resource_group_name, service_name, product_id, api_id, custom_headers:nil)
      response = remove_async(resource_group_name, service_name, product_id, api_id, custom_headers:custom_headers).value!
      nil
    end