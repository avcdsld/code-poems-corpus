def update_repair_task_health_policy(repair_task_update_health_policy_description, custom_headers:nil)
      response = update_repair_task_health_policy_async(repair_task_update_health_policy_description, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end