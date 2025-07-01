def get_with_http_info(resource_group_name, profile_name, endpoint_name, custom_domain_name, custom_headers:nil)
      get_async(resource_group_name, profile_name, endpoint_name, custom_domain_name, custom_headers:custom_headers).value!
    end