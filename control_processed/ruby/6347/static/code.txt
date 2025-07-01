def report_node_health_with_http_info(node_name, health_information, immediate:false, timeout:60, custom_headers:nil)
      report_node_health_async(node_name, health_information, immediate:immediate, timeout:timeout, custom_headers:custom_headers).value!
    end