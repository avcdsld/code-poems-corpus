def download_updates(device_name, resource_group_name, custom_headers:nil)
      response = download_updates_async(device_name, resource_group_name, custom_headers:custom_headers).value!
      nil
    end