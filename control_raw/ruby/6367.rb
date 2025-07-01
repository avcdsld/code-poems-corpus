def get_service_type_info_list_with_http_info(application_type_name, application_type_version, timeout:60, custom_headers:nil)
      get_service_type_info_list_async(application_type_name, application_type_version, timeout:timeout, custom_headers:custom_headers).value!
    end