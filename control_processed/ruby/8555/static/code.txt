def update_with_http_info(resource_group_name, application_name, parameters:nil, custom_headers:nil)
      update_async(resource_group_name, application_name, parameters:parameters, custom_headers:custom_headers).value!
    end