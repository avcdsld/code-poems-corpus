def get_ip_filter_rule_with_http_info(resource_group_name, namespace_name, ip_filter_rule_name, custom_headers:nil)
      get_ip_filter_rule_async(resource_group_name, namespace_name, ip_filter_rule_name, custom_headers:custom_headers).value!
    end