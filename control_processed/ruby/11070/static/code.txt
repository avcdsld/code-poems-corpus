def get_available_operations(custom_headers:nil)
      response = get_available_operations_async(custom_headers:custom_headers).value!
      response.body unless response.nil?
    end