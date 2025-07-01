def cancel_repair_task(repair_task_cancel_description, custom_headers:nil)
      response = cancel_repair_task_async(repair_task_cancel_description, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end