def enable_monitoring(resource_group_name, hana_instance_name, monitoring_parameter, custom_headers:nil)
      response = enable_monitoring_async(resource_group_name, hana_instance_name, monitoring_parameter, custom_headers:custom_headers).value!
      nil
    end