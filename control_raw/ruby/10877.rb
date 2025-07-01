def list_post_authorization_rules_with_http_info(resource_group_name, namespace_name, relay_name, custom_headers:nil)
      list_post_authorization_rules_async(resource_group_name, namespace_name, relay_name, custom_headers:custom_headers).value!
    end