def update_with_http_info(resource_group_name, automation_account_name, module_name, parameters, custom_headers:nil)
      update_async(resource_group_name, automation_account_name, module_name, parameters, custom_headers:custom_headers).value!
    end