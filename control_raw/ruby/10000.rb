def create_with_http_info(resource_group_name, account_name, transform_name, job_name, parameters, custom_headers:nil)
      create_async(resource_group_name, account_name, transform_name, job_name, parameters, custom_headers:custom_headers).value!
    end