def get_credentials(resource_group_name, registry_name, custom_headers:nil)
      response = get_credentials_async(resource_group_name, registry_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end