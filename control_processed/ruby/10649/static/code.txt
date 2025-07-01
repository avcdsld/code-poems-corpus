def get_monitoring_status(resource_group_name, cluster_name, custom_headers:nil)
      response = get_monitoring_status_async(resource_group_name, cluster_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end