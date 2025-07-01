def list_by_api_with_http_info(resource_group_name, service_name, api_id, custom_headers:nil)
      list_by_api_async(resource_group_name, service_name, api_id, custom_headers:custom_headers).value!
    end