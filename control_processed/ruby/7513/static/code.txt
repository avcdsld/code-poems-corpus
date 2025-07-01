def export_request_rate_by_interval(parameters, location, custom_headers:nil)
      response = export_request_rate_by_interval_async(parameters, location, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end