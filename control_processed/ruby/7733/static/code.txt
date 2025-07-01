def begin_update_with_http_info(resource_group_name, resource_name, app_patch, custom_headers:nil)
      begin_update_async(resource_group_name, resource_name, app_patch, custom_headers:custom_headers).value!
    end