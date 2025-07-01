def begin_replace_content(resource_group_name, automation_account_name, runbook_name, runbook_content, custom_headers:nil)
      response = begin_replace_content_async(resource_group_name, automation_account_name, runbook_name, runbook_content, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end