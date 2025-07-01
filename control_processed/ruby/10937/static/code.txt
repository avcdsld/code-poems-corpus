def regenerate(resource_group_name, search_service_name, key_kind, search_management_request_options:nil, custom_headers:nil)
      response = regenerate_async(resource_group_name, search_service_name, key_kind, search_management_request_options:search_management_request_options, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end