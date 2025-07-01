def check_name_availability_method_with_http_info(resource_group_name, namespace_name, parameters, custom_headers:nil)
      check_name_availability_method_async(resource_group_name, namespace_name, parameters, custom_headers:custom_headers).value!
    end