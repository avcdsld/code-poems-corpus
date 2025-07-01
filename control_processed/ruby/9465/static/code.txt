def list_orchestrators(location, resource_type:nil, custom_headers:nil)
      response = list_orchestrators_async(location, resource_type:resource_type, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end