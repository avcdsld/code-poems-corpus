def set_legal_hold_with_http_info(resource_group_name, account_name, container_name, legal_hold, custom_headers:nil)
      set_legal_hold_async(resource_group_name, account_name, container_name, legal_hold, custom_headers:custom_headers).value!
    end