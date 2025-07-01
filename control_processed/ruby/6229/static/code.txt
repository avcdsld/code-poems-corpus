def set_legal_hold(resource_group_name, account_name, container_name, legal_hold, custom_headers:nil)
      response = set_legal_hold_async(resource_group_name, account_name, container_name, legal_hold, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end