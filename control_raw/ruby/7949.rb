def trigger(vault_name, resource_group_name, job_name, custom_headers:nil)
      response = trigger_async(vault_name, resource_group_name, job_name, custom_headers:custom_headers).value!
      nil
    end