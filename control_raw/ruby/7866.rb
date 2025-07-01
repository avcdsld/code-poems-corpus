def get_with_http_info(resource_group_name, service_name, identity_provider_name, custom_headers:nil)
      get_async(resource_group_name, service_name, identity_provider_name, custom_headers:custom_headers).value!
    end