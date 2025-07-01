def stop_with_http_info(resource_group_name, automation_account_name, job_id, custom_headers:nil)
      stop_async(resource_group_name, automation_account_name, job_id, custom_headers:custom_headers).value!
    end