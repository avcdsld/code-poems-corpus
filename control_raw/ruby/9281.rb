def list_by_resource_group_with_http_info(resource_group_name, expand:nil, filter:nil, top:nil, orderby:nil, custom_headers:nil)
      list_by_resource_group_async(resource_group_name, expand:expand, filter:filter, top:top, orderby:orderby, custom_headers:custom_headers).value!
    end