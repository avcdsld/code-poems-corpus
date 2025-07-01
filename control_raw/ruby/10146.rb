def check_notification_hub_availability_with_http_info(resource_group_name, namespace_name, parameters, custom_headers:nil)
      check_notification_hub_availability_async(resource_group_name, namespace_name, parameters, custom_headers:custom_headers).value!
    end