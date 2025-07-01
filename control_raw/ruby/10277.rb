def update_ownership_identifier_with_http_info(resource_group_name, domain_name, name, domain_ownership_identifier, custom_headers:nil)
      update_ownership_identifier_async(resource_group_name, domain_name, name, domain_ownership_identifier, custom_headers:custom_headers).value!
    end