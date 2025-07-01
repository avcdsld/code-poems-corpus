def supported_security_providers(resource_group_name, virtual_wanname, custom_headers:nil)
      response = supported_security_providers_async(resource_group_name, virtual_wanname, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end