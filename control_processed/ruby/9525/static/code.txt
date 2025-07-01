def list_feature_support_status_with_http_info(resource_group_name, manager_name, filter:nil, custom_headers:nil)
      list_feature_support_status_async(resource_group_name, manager_name, filter:filter, custom_headers:custom_headers).value!
    end