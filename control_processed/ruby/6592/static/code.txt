def get_service_backup_configuration_info_with_http_info(service_id, continuation_token:nil, max_results:0, timeout:60, custom_headers:nil)
      get_service_backup_configuration_info_async(service_id, continuation_token:continuation_token, max_results:max_results, timeout:timeout, custom_headers:custom_headers).value!
    end