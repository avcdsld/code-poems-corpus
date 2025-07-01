def get_ownership_identifier(resource_group_name, domain_name, name, custom_headers:nil)
      response = get_ownership_identifier_async(resource_group_name, domain_name, name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end