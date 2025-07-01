def get_deployed_application_info(node_name, application_id, timeout:60, include_health_state:false, custom_headers:nil)
      response = get_deployed_application_info_async(node_name, application_id, timeout:timeout, include_health_state:include_health_state, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end