def list(application_resource_name, service_resource_name, custom_headers:nil)
      response = list_async(application_resource_name, service_resource_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end