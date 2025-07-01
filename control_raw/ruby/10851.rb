def get_with_http_info(resource_group_name, server_name, job_agent_name, job_name, job_execution_id, step_name, custom_headers:nil)
      get_async(resource_group_name, server_name, job_agent_name, job_name, job_execution_id, step_name, custom_headers:custom_headers).value!
    end