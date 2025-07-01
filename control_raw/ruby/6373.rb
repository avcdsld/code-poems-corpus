def get_deployed_service_type_info_list_with_http_info(node_name, application_id, service_manifest_name:nil, timeout:60, custom_headers:nil)
      get_deployed_service_type_info_list_async(node_name, application_id, service_manifest_name:service_manifest_name, timeout:timeout, custom_headers:custom_headers).value!
    end