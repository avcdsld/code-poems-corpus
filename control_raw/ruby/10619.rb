def get_update_summary(device_name, resource_group_name, custom_headers:nil)
      response = get_update_summary_async(device_name, resource_group_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end