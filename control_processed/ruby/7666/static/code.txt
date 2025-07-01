def begin_create_or_update_multi_role_pool_with_http_info(resource_group_name, name, multi_role_pool_envelope, custom_headers:nil)
      begin_create_or_update_multi_role_pool_async(resource_group_name, name, multi_role_pool_envelope, custom_headers:custom_headers).value!
    end