def create_or_update_with_http_info(resource_group_name, automation_account_name, connection_type_name, parameters, custom_headers:nil)
      create_or_update_async(resource_group_name, automation_account_name, connection_type_name, parameters, custom_headers:custom_headers).value!
    end