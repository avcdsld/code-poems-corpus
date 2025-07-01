def delete_with_http_info(resource_group_name, hub_name, assignment_name, custom_headers:nil)
      delete_async(resource_group_name, hub_name, assignment_name, custom_headers:custom_headers).value!
    end