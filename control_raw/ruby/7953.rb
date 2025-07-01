def delete(resource_group_name, activity_log_alert_name, custom_headers:nil)
      response = delete_async(resource_group_name, activity_log_alert_name, custom_headers:custom_headers).value!
      nil
    end