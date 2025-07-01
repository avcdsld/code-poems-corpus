def invoke_infrastructure_command_with_http_info(command, service_id:nil, timeout:60, custom_headers:nil)
      invoke_infrastructure_command_async(command, service_id:service_id, timeout:timeout, custom_headers:custom_headers).value!
    end