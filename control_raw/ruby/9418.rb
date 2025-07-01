def create(resource_group_name, profile_name, endpoint_name, custom_domain_name, custom_domain_properties, custom_headers:nil)
      response = create_async(resource_group_name, profile_name, endpoint_name, custom_domain_name, custom_domain_properties, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end