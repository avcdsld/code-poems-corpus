def begin_unplanned_failover(recovery_plan_name, input, custom_headers:nil)
      response = begin_unplanned_failover_async(recovery_plan_name, input, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end