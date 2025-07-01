def update(recovery_plan_name, input, custom_headers:nil)
      response = update_async(recovery_plan_name, input, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end