def create_or_update_network_rule_set_with_http_info(resource_group_name, namespace_name, parameters, custom_headers:nil)
      create_or_update_network_rule_set_async(resource_group_name, namespace_name, parameters, custom_headers:custom_headers).value!
    end