def execute(name_availability_request, custom_headers:nil)
      response = execute_async(name_availability_request, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end