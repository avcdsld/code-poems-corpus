def list_hybrid_connection_keys_with_http_info(resource_group_name, name, namespace_name, relay_name, custom_headers:nil)
      list_hybrid_connection_keys_async(resource_group_name, name, namespace_name, relay_name, custom_headers:custom_headers).value!
    end