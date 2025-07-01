def list_regional_by_resource_group_with_http_info(resource_group_name, location, filter:nil, top:nil, label:nil, custom_headers:nil)
      list_regional_by_resource_group_async(resource_group_name, location, filter:filter, top:top, label:label, custom_headers:custom_headers).value!
    end