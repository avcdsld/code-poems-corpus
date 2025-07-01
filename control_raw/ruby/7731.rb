def check_name_availability(operation_inputs, custom_headers:nil)
      response = check_name_availability_async(operation_inputs, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end