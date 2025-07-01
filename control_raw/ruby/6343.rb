def get_node_health_with_http_info(node_name, events_health_state_filter:0, timeout:60, custom_headers:nil)
      get_node_health_async(node_name, events_health_state_filter:events_health_state_filter, timeout:timeout, custom_headers:custom_headers).value!
    end