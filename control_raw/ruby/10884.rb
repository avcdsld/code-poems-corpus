def list_usage_scenarios(custom_headers:nil)
      response = list_usage_scenarios_async(custom_headers:custom_headers).value!
      response.body unless response.nil?
    end