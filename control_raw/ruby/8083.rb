def get_with_http_info(resource_group_name, automation_account_name, runbook_name, custom_headers:nil)
      get_async(resource_group_name, automation_account_name, runbook_name, custom_headers:custom_headers).value!
    end