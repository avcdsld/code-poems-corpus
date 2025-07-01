def begin_export_throttled_requests(parameters, location, custom_headers:nil)
      response = begin_export_throttled_requests_async(parameters, location, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end