def list_paths_with_http_info(resource_group_name, account_name, streaming_locator_name, custom_headers:nil)
      list_paths_async(resource_group_name, account_name, streaming_locator_name, custom_headers:custom_headers).value!
    end