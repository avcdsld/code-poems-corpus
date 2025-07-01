def enable_custom_https(resource_group_name, profile_name, endpoint_name, custom_domain_name, custom_headers:nil)
      response = enable_custom_https_async(resource_group_name, profile_name, endpoint_name, custom_domain_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end