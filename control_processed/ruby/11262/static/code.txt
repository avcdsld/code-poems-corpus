def get_default(custom_headers:nil)
      response = get_default_async(custom_headers:custom_headers).value!
      response.body unless response.nil?
    end