def restart_deployed_code_package_with_http_info(node_name, application_id, restart_deployed_code_package_description, timeout:60, custom_headers:nil)
      restart_deployed_code_package_async(node_name, application_id, restart_deployed_code_package_description, timeout:timeout, custom_headers:custom_headers).value!
    end