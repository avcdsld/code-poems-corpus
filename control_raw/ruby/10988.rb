def create_with_http_info(resource_group_name, service_name, product_id, group_id, custom_headers:nil)
      create_async(resource_group_name, service_name, product_id, group_id, custom_headers:custom_headers).value!
    end