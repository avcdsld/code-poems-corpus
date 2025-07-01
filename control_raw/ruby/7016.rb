def create_with_http_info(scope, role_assignment_name, parameters, custom_headers:nil)
      create_async(scope, role_assignment_name, parameters, custom_headers:custom_headers).value!
    end