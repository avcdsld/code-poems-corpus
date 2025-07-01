def get_service_info_list(application_id, service_type_name:nil, continuation_token:nil, timeout:60, custom_headers:nil)
      response = get_service_info_list_async(application_id, service_type_name:service_type_name, continuation_token:continuation_token, timeout:timeout, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end