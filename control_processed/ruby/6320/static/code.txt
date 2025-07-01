def get_cluster_configuration_with_http_info(configuration_api_version, timeout:60, custom_headers:nil)
      get_cluster_configuration_async(configuration_api_version, timeout:timeout, custom_headers:custom_headers).value!
    end