def regenerate_secret_key_with_http_info(resource_group_name, workflow_name, access_key_name, parameters, custom_headers:nil)
      regenerate_secret_key_async(resource_group_name, workflow_name, access_key_name, parameters, custom_headers:custom_headers).value!
    end