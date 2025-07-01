def create_or_update_firewall_rule_with_http_info(resource_group_name, account_name, name, parameters, custom_headers:nil)
      create_or_update_firewall_rule_async(resource_group_name, account_name, name, parameters, custom_headers:custom_headers).value!
    end