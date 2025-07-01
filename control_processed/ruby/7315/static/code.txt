def get_properties_with_http_info(resource_group_name, account_name, expand:nil, custom_headers:nil)
      get_properties_async(resource_group_name, account_name, expand:expand, custom_headers:custom_headers).value!
    end