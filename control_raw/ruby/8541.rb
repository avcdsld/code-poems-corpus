def delete_with_http_info(resource_group_name, server_name, firewall_rule_name, custom_headers:nil)
      delete_async(resource_group_name, server_name, firewall_rule_name, custom_headers:custom_headers).value!
    end